#!/usr/bin/python

import re
from random import choice
from en import verb
from nltk.tree import ParentedTree
from nltk.corpus import wordnet as wn
from stanfordcorenlp import StanfordCoreNLP
import pdb

global chunked_sent
global chunked_tree
global verb_chunks
global verb_tree
global found_pred
global found_subj
global subj_phrase
global pred_phrase
global obj_phrase
# global verbs_pos
# global auxillary_verbs

nlp = StanfordCoreNLP(r'C:\nltk_data\stanford-corenlp-full-2017-06-09\stanford-corenlp-full-2017-06-09')

verbs_pos = [u'VB', u'VBZ', u'VBP', u'VBN', u'VBG', u'VBD', u'MD']
auxillary_verbs = ['be', 'am', 'are', 'is', 'was', 'were', 'being', 'been', \
                   'can', 'could', 'dare', 'do', 'does', 'did', 'have', \
                   'has', 'had', 'having', 'may', 'might', 'must', 'need', \
                   'ought', 'shall', 'should', 'will', 'would']


class GeneratedQuestion:
    def __init__(self, fact):
        self.fact = fact
        self.fact_tree = None
        self.found_pred = 0
        self.found_subj = 0
        self.chunked_sent = []
        self.chunked_tree = []
        self.verb_chunks = []
        self.verb_tree = []
        self.subj_phrase = []
        self.pred_phrase = []
        self.obj_phrase = []
        self.answer_list = []
        self.question_list = []
        
    def __repr__(self):
        return "Chunked Sentence: {0}\nChunked Tree: {1}\nVerb Chunks: {2}\nVerb Tree: {3}\nSubject " \
               "Phrase: {4}\nPredicate Phrase: {5}\nObject Phrase: {6}\n".format(self.chunked_sent , self.chunked_tree,
                                                                                 self.verb_chunks, self.verb_tree,
                                                                                 self.subj_phrase, self.pred_phrase,
                                                                                 self.obj_phrase)
    
    def get_tree(self):
        print("Inside get tree ++++++++")
        """
        Given a single statement, parse and return a tree
        :param fact: The statement
        :return: a parse tree representing the fact
        """
    
        tree_chunk = nlp.parse(self.fact)
        print("Tree chunk+++++++", tree_chunk)
        parse_tree_text = ""
        tree = ""
        for line in tree_chunk:
            if "(. .)))" in line:
                tree += ')'
                parse_tree_text = tree
                tree = ""
            else:
                tree = tree + line
    
        # return ParentedTree.fromstring(tree)
        self.fact_tree = ParentedTree.fromstring(tree)
        print("Fact tree from the get ree method+++++++ ",self.fact_tree)

    def traverse_and_chunk(self):
        print("Inside traverse_and_chunk ++++++++")
        try:
            self.fact_tree.label()
        except AttributeError:
            return
        else:
            #if label is NP then 
            #pdb.set_trace()
            for i, np_tree in enumerate(self.fact_tree.subtrees(filter=lambda x: x.label() == 'NP')):
                #add np_tree POS in small case to chunked_tree
                self.chunked_tree.append(format_pos_tuples(np_tree.pos()))
                chunk_phrase = np_tree.leaves()
                #add noun in small case to lowercase_chunk_phrase
                lowercase_chunk_phrase = [make_lower(val) for val in chunk_phrase]
                # self.chunked_sent.append((u'NP', chunk_phrase))
                #add NP and lowercase_chunk_phrase to chunked_sent
                self.chunked_sent.append((u'NP', lowercase_chunk_phrase))
    
            for j, pp_tree in enumerate(self.fact_tree.subtrees(filter=lambda x: x.label() == 'PP')):
                self.chunked_tree.append(format_pos_tuples(pp_tree.pos()))
                chunk_phrase = pp_tree.leaves()
                lowercase_chunk_phrase = [make_lower(val) for val in chunk_phrase]
                # self.chunked_sent.append((u'PP', chunk_phrase))
                self.chunked_sent.append((u'PP', lowercase_chunk_phrase))
                pp_object_trees = [np for np in pp_tree.subtrees(filter=lambda x: x.label() == 'NP')]
    
            for k, sbar_tree in enumerate(self.fact_tree.subtrees(filter=lambda x: x.label() == 'SBAR')):
                self.chunked_tree.append(format_pos_tuples(sbar_tree.pos()))
                chunk_phrase = sbar_tree.leaves()
                lowercase_chunk_phrase = [make_lower(val) for val in chunk_phrase]
                # self.chunked_sent.append((u'SBAR', chunk_phrase))
                self.chunked_sent.append((u'SBAR', lowercase_chunk_phrase))
    
            for n, vp_tree in enumerate(self.fact_tree.subtrees(filter=lambda x: x.label() == 'VP')):
                self.verb_tree.append(format_pos_tuples(vp_tree.pos()))
                chunk_phrase = vp_tree.leaves()
                lowercase_chunk_phrase = [make_lower(val) for val in chunk_phrase]
                self.verb_chunks.append((u'VP', lowercase_chunk_phrase))
    
            '''
            When a parse tree is created for a declarative sentence,
            the subject of a sentence is (usually) the leftmost
            first level subtree (specified by 0,0)
            The predicate is the rightmost first level subtree
            (specified by 0, 1). The object is the first noun phrase
            in the predicate verb phrase
            '''
    
            # self.subj_phrase = self.fact_tree[(0,0)].leaves()
            self.subj_phrase = [make_lower(val) for val in self.fact_tree[(0, 0)].leaves()]
            # self.pred_phrase = self.fact_tree[(0,1)].leaves()
            self.pred_phrase = [make_lower(val) for val in self.fact_tree[(0, 1)].leaves()]
            np_obj_trees = [np for np in self.fact_tree[0, 1].subtrees(filter=lambda x: x.label() == 'NP')]
            print(np_obj_trees)
            if np_obj_trees:
                self.obj_phrase = [make_lower(val) for val in np_obj_trees[0].leaves()]
            # need to remove commas
            # pruned_leaves = [leaf for leaf in np_obj_trees[0].leaves() if leaf is not ',']
            # print(pruned_leaves)
            # self.obj_phrase = [make_lower(val) for val in pruned_leaves]
            '''
    
            #self.subj_phrase = self.fact_tree[(0,0)].leaves()
            self.subj_phrase = [make_lower(val) for val in self.fact_tree[(0,0)].leaves()]
    
            bad_tree_indicators = [',', '.', 'CC'] 
            for tree_index in range(1, len(self.fact_tree[0])): #remove
                if self.fact_tree[(0, tree_index)].label() not in bad_tree_indicators:
                    self.pred_phrase = [make_lower(val) for val in self.fact_tree[(0,tree_index)].leaves()]
                    np_obj_trees = [np for np in self.fact_tree[0,tree_index].subtrees(filter=lambda x: x.label() == 'NP')]
                    print('subtree')
                    print(self.fact_tree[0,tree_index])
                    print(np_obj_trees[0].leaves())
                else:
                    continue
            '''

    def apply_rules(self):
        print("Inside apply_rules ++++++++")
        # if we find a colon, apply rule_colon
        match = re.search(':', self.fact)
        if match:
            question, answer = self.rule_colon(self.fact)

            # check for duplicate questions
            if question not in self.question_list or answer not in self.answer_list:
                self.question_list.append(question)
                self.answer_list.append(answer)

        # if we find a "because" clause, apply rule_because
        match = re.search('because', self.fact)
        if match:
            # self.question_list, self.answer_list = rule_because(self.fact)
            question, answer = self.rule_because(self.fact)

            # check for duplicate questions
            if question not in self.question_list or answer not in self.answer_list:
                self.question_list.append(question)
                self.answer_list.append(answer)

        # apply subject predicate inversion
        question, answer = self.rule_subj_pred_inversion()
        if question not in self.question_list or answer not in self.answer_list:
            self.question_list.append(question)
            self.answer_list.append(answer)

        # apply predicate decomposition
        question, answer = self.rule_pred_decompositon()
        if question not in self.question_list or answer not in self.answer_list:
            self.question_list.append(question)
            self.answer_list.append(answer)

        # apply verb object
        # print(self.verb_tree)
        # print(verb_chunks)
        # for tuple_list in chunked_tree:
        for tuple_list in self.verb_tree:
            for word, pos in tuple_list:
                # print(word, pos)
                if pos == 'VBN':
                    question, answer = self.rule_verb_object(word)
                    if question not in self.question_list or answer not in self.answer_list:
                        self.question_list.append(question)
                        self.answer_list.append(answer)

        '''
        The chunked_sent is a list of tuples.  The first value is the part of speech
        for the chunk; the second value is a list of the words in the chunk

        chunked_tree is also a list of tuples generated from the same tree that the
        chunked_sent is generated from, but for the individual words in the tree.
        The first value is the part of speech of the word and the second value is the
        word itself.

        e.g.  a value from chunked_sent =
            (u'NP', ['the', 'ability', 'to', 'monitor', 'changes']) 
        e.g.  a correpsonding value from chunked_tree =
            [('The', 'DT'), ('ability', 'NN'), ('to', 'TO'), ('monitor', 'VB'), ('changes', 'NNS')]
        '''
        # for ntype, c in candidate_nodes:
        for ntype_word_list, pos_tuples_list in zip(self.chunked_sent, self.chunked_tree):

            ntype = ntype_word_list[0]
            chunk = ntype_word_list[1]
            pos_chunk = pos_tuples_list

            if ntype == u'NP':
                question, answer = self.rule_chunk_np(chunk, pos_chunk, self.fact)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

            elif ntype == u'SBAR':
                question, answer = self.rule_chunk_sbar(chunk)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

            elif ntype == u'PP':
                question, answer = self.rule_chunk_pp(chunk, pos_chunk, self.fact)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

        # add subject verb insertion
        # e.g Decision makers are affected by many of the same emotions applied in personal purchases.
        # makes What are decision makers affected by?

        # apply verb object
        for tuple_list in self.verb_tree:
            for word, pos in tuple_list:
                # print(word, pos)
                if pos == 'VBN':
                    question, answer = self.rule_verb_object(word)
                    if question not in self.question_list or answer not in self.answer_list:
                        self.question_list.append(question)
                        self.answer_list.append(answer)

        '''
        The chunked_sent is a list of tuples.  The first value is the part of speech
        for the chunk; te second value is a list of the words in the chunk

        chunked_tree is also a list of tuples generated from the same tree that the
        chunked_sent is generated from, but for the individual words in the tree.
        The first value is the part of speech of the word and the second value is the
        word itself.

        e.g.  a value from chunked_sent =
            (u'NP', ['the', 'ability', 'to', 'monitor', 'changes']) 
        e.g.  a correpsonding value from chunked_tree =
            [('The', 'DT'), ('ability', 'NN'), ('to', 'TO'), ('monitor', 'VB'), ('changes', 'NNS')]
        '''
        # for ntype, c in candidate_nodes:
        for ntype_word_list, pos_tuples_list in zip(self.chunked_sent, self.chunked_tree):

            ntype = ntype_word_list[0]
            chunk = ntype_word_list[1]
            pos_chunk = pos_tuples_list

            if ntype == u'NP':
                question, answer = self.rule_chunk_np(chunk, pos_chunk, self.fact)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

            elif ntype == u'SBAR':
                question, answer = self.rule_chunk_sbar(chunk)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

            elif ntype == u'PP':
                question, answer = self.rule_chunk_pp(chunk, pos_chunk, self.fact)
                if question not in self.question_list or answer not in self.answer_list:
                    self.question_list.append(question)
                    self.answer_list.append(answer)

    # if we find a colon, generate a question automatically
    def rule_colon(self, full_fact):
        print("Inside rule_colon ++++++++")
        # global auxillary_verbs
        fact = format_fact(full_fact)

        fact_parts = re.split(':', fact)  # extra space added for formatting
        print(fact_parts)
        answer = fact_parts[1]
        if pred_phrase[0] in auxillary_verbs:
            # strippedPart = re.sub(predicatePhrase[0], '', factParts[0])
            regexp = "\\b%s\\b" % pred_phrase[0]  # added to guard against verbs like 'is'
            strippedPart = re.sub(regexp, '', fact_parts[0])
            #question = 'What ' + pred_phrase[0] + ' ' + strippedPart + '? --> rule_colon'
            question = 'What ' + pred_phrase[0] + ' ' + strippedPart + '?'
        else:
            #question = 'What does ' + fact_parts[0] + '?' + ' --> rule_colon'
            question = 'What does ' + fact_parts[0] + '?'

        return (question, answer)

    # if we find a "because fact", generate a question automatically
    def rule_because(self, full_fact):
        print("Inside rule_because ++++++++")
        # global auxillary_verbs
        fact = format_fact(full_fact)

        factParts = re.split(' because ', fact)  # extra space added for formatting
        answer = factParts[1]
        if self.pred_phrase[0] in auxillary_verbs:
            # strippedPart = re.sub(predicatePhrase[0], '', factParts[0])
            regexp = "\\b%s\\b" % self.pred_phrase[0]  # added to guard against verbs like 'is'
            strippedPart = re.sub(regexp, '', factParts[0])
            #question = 'Why ' + self.pred_phrase[0] + ' ' + strippedPart + '? --> rule_because'
            question = 'Why ' + self.pred_phrase[0] + ' ' + strippedPart + '?'
        else:
            #question = 'Why does ' + factParts[0] + '?' + ' --> rule_because'
            question = 'Why does ' + factParts[0] + '?'

        return (question, answer)


    # apply subject predicate inversion
    def rule_subj_pred_inversion(self):
        print("Inside rule_subj_pred_inversion ++++++++")
        # global subj_phrase
        # global pred_phrase
        # global chunked_tree
        # global auxillary_verbs

        head_word = determine_head_word(self.subj_phrase, self.chunked_tree[0])
        wh_term = determine_wh_word(head_word)

        if wh_term == 'What':
            question_root = choice(['Which of the following', 'What'])
        else:
            question_root = wh_term

        answer = " ".join(self.subj_phrase)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        rawQuestion = " ".join(self.pred_phrase)
        #question = question_root + ' ' + rawQuestion + '?' + ' --> sub_pred_inversion'
        question = question_root + ' ' + rawQuestion + '?'

        return (question, answer)

    def rule_pred_decompositon(self):
        print("Inside rule_pred_decompositon ++++++++")
        # global subj_phrase
        # global pred_phrase
        # global auxillary_verbs
        # global obj_phrase

        head_word = determine_head_word(self.subj_phrase, self.chunked_tree[0])
        wh_term = determine_wh_word(head_word)

        if wh_term == 'What':
            question_root = choice(['Which of the following', 'What'])
        else:
            question_root = wh_term

        answer = " ".join(self.obj_phrase)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        rawQuestion = " ".join(self.subj_phrase)

        vbn_word = self.pred_phrase[0]

        # if word is in auxillary verbs apply do
        if vbn_word not in auxillary_verbs:
            do_verb = match_verb_tense(vbn_word, 'do')
            # tense_command = 'verb.' + str(tense) + '("do")'
            # do_verb = eval(tense_command)
            #question = question_root + ' ' + do_verb + ' ' + rawQuestion + ' ' + vbn_word + '?' + ' --> pred_decomp'
            question = question_root + ' ' + do_verb + ' ' + rawQuestion + ' ' + vbn_word + '?'
        else:
            #question = question_root + ' ' + self.pred_phrase[0] + ' ' + rawQuestion + ' ' + self.pred_phrase[1] + '?' + ' --> pred_decomp'
            question = question_root + ' ' + self.pred_phrase[0] + ' ' + rawQuestion + ' ' + self.pred_phrase[1] + '?'
        return (question, answer)


    def rule_verb_object(self, vbn_word):
        print("Inside rule_verb_object ++++++++")
        # global subj_phrase
        # global obj_phrase
        #
        # head_word = determine_head_word(subj_phrase, chunked_tree[0])
        # wh_term = determine_wh_word(head_word)

        # print('rule verb object')
        question_root = choice(['Which of the following', 'What'])

        answer = " ".join(self.obj_phrase)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        present_vbn = verb.present(vbn_word, person=3, negate=False)

        rawQuestion = " ".join(self.subj_phrase)
        # question = question_root + ' ' + vbn_word + ' ' + rawQuestion + '?'
        #question = question_root + ' ' + present_vbn + ' ' + rawQuestion + '?' + ' --> verb_object'
        question = question_root + ' ' + present_vbn + ' ' + rawQuestion + '?'
        return (question, answer)

    '''
    Chunk rules are designed to be applied to sentence chunks
    Therefore, the only return single answers and questions
    '''

    def rule_chunk_sbar(self, chunk):
        print("Inside rule_chunk_sbar ++++++++")
        # global subj_phrase

        question_root = choice(['Which of the following', 'What'])
        questionFrag = chunk[2:]

        answer = " ".join(self.subj_phrase)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        rawQuestion = " ".join(questionFrag)
        # question = question_root + ' ' + rawQuestion + '?'
        #question = question_root + ' ' + rawQuestion + '?' + ' --> rule_sbar'
        question = question_root + ' ' + rawQuestion + '?'
        return (question, answer)


    def rule_chunk_pp(self, chunk, pos_chunk, full_fact):
        print("Inside rule_chunk_pp ++++++++")
        global subj_phrase
        global pred_phrase
        global obj_phrase
        # global auxillary_verbs

        '''
        head_word = determine_head_word(chunk, pos_chunk)

        wh_term = determine_wh_word(head_word)

        if wh_term == 'What':
            question_root = choice(['Which of the following', 'What'])
        else:
            question_root = wh_term

        fact = format_fact(full_fact)
        '''

        answer = " ".join(chunk)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        question_subject = " ".join(self.subj_phrase)

        stripped_fact = re.sub('\.', '', full_fact)  # remove period
        stripped_fact = re.sub('\n', '', stripped_fact)  # remove period
        stripped_fact = re.sub(answer, '', stripped_fact)
        # stripped_fact = stripped_fact[:-1]
        stripped_fact.rstrip()

        # print('PP')
        # print(chunk[0])

        '''
        if chunk[0] == 'because':
            modifier = ' of '
        else:
            modifier = ''
        '''
        #question = stripped_fact + chunk[0] + ' which of the following?' + ' --> rule_pp'
        question = stripped_fact + chunk[0] + ' which of the following?'
        return (question, answer)


    def rule_chunk_np(self, chunk, pos_chunk, full_fact):
        print("Inside rule_chunk_np ++++++++")
        # global subj_phrase
        # global pred_phrase
        # global obj_phrase
        # global auxillary_verbs

        head_word = determine_head_word(chunk, pos_chunk)
        wh_term = determine_wh_word(head_word)

        if wh_term == 'What':
            question_root = choice(['Which of the following', 'What'])
        else:
            question_root = wh_term

        fact = format_fact(full_fact)

        answer = " ".join(chunk)
        answer = re.sub(' \,', ',', answer)  # remove spaces before comma

        question_subject = " ".join(self.subj_phrase)

        if answer == question_subject:
            question_subject = " ".join(self.obj_phrase)

        try:
            question_predicate = " ".join(self.pred_phrase) if len(self.pred_phrase) > 1 else self.pred_phrase[0]
        except:
            print(fact)
            print("Length of predicate phrase: " + str(len(self.pred_phrase)))
            exit(1)

        if self.pred_phrase[0] in auxillary_verbs and len(self.pred_phrase) > 1:
            # question_head =  question_root + ' ' + pred_phrase[0] + ' ' + question_subject + ' ' + pred_phrase[1] + ' '
            question = question_root + ' ' + self.pred_phrase[0] + ' ' + question_subject + ' ' + self.pred_phrase[1] + ' '
        else:
            # question_head = question_root + ' ' + pred_phrase[0] + ' ' + question_subject + ' '
            question = question_root + ' ' + self.pred_phrase[0] + ' ' + question_subject + ' '

        '''
        stripped_fact = re.sub(answer, '', fact)
        regexp = "\\b%s\\b" % question_subject
        stripped_fact = re.sub(regexp, '', stripped_fact)
        regexp = "\\b%s\\b" % question_predicate
        stripped_fact = re.sub(regexp, '', stripped_fact)
        question = question_head + stripped_fact
        question = re.sub('   ', ' ', question)
        question = re.sub('  ', ' ', question)
        '''

        if question[-1] == ' ':
            question = question[:-1]

        #question = question + '?' + ' --> rule_np'
        question = question + '?'

        return (question, answer)


def make_lower(arg_string):
    print("Inside make_lower ++++++++")
    return arg_string.lower()


def format_fact(full_fact):
    print("Inside format_fact ++++++++")
    fact = full_fact.lower()
    fact = re.sub('\n', '', fact)  # remove trailing newline
    fact = re.sub('\.', '', fact)  # remove period
    return fact


# convert any word in the POS tuple to lowercase
def format_pos_tuples(tup_list):
    print("Inside format_pos_tuples ++++++++")
    lowercase_list = [(make_lower(word), pos) for word, pos in tup_list]
    return lowercase_list


def replaceUnicodeChars(str):
    print("Inside replaceUnicodeChars ++++++++")
    preStr = re.sub('[^a-z^A-Z^ ^\n^/-]*', '', str)
    return re.sub('(\n)', ' ', preStr)


def write_questions_and_answers(item_number, original_fact, question_list, answer_list,
                                output_file='questions.txt'):
    print("Inside write_questions_and_answers ++++++++")

    item_file = open(output_file, 'w')

    if len(question_list) != len(answer_list):
        raise Exception('question list length and answer list length do not match')

    statusStr = "Item %d" % (item_number)
    print(statusStr)
    print('--------')
    print(original_fact + '\n')

    #item_file.write(statusStr + '\n')
    #item_file.write('--------\n')
    #item_file.write(original_fact + '\n\n')

    for q_and_a in zip(question_list, answer_list):
        print('Q: ' + q_and_a[0])
        print('A: ' + q_and_a[1] + '\n')

        item_file.write(q_and_a[0] + '\n\n')
        #item_file.write('A: ' + q_and_a[1] + '\n\n')

    item_file.close()


def determine_head_word(chunk, pos_chunk):
    print("Inside determine_head_word ++++++++")
    nns_flag = 0
    nn_flag = 0
    jj_flag = 0

    for word, pos in pos_chunk:
        if word in chunk:
            # check part of speech
            if pos == 'NNS' and nns_flag == 0:
                nns_flag = 1
                nns_word = word
            elif pos == 'NN' and nn_flag == 0:
                nn_flag = 1
                nn_word = word
            elif pos == 'JJ' and jj_flag == 0:
                jj_flag = 1
                jj_word = word
        else:
            raise Exception('Could not find word in chunk -- check chunk and pos_chunk for match')

    if nns_flag == 1:
        return nns_word
    elif nn_flag == 1:
        return nn_word
    elif jj_flag == 1:
        return jj_word
    else:
        return 'foobar'  # pos not in noun list and not JJ


def determine_wh_word(term):
    print("Inside determine_wh_word ++++++++")
    # for synset in wn.synsets(term):

    # handle error case
    if term == 'foobar':
        return 'What'

    # use the first synset sense to determine noun type
    first_synset = wn.synsets(term)[0]

    if first_synset is not None:  # test for existence, may have None type if no synset
        if first_synset.lexname() == u'noun.person':
            return 'Who'
        elif first_synset.lexname() == u'noun.location':
            return 'Where'
        elif first_synset.lexname() == u'noun.time':
            return 'When'
        else:
            return 'What'
    else:
        print("\nWarning: no synset found for %s. Returning 'What'\n" % term)
        return 'What'


def match_verb_tense(input_verb, verb_to_match):
    print("Inside match_verb_tense ++++++++")
    present_tenses = ['1st singular present', '2nd singular present', '3rd singular present']
    past_tenses = ['1st singular past', '2nd singular past', '3rd singular past']

    try:
        verb_tense = verb.tense(input_verb)
    except KeyError:
        print(
        "WARNING: Could not find a verb tense for %s. Returning the verb to match without modification." % (input_verb))
        return verb_to_match

    if verb_tense == 'infinitive':
        match = verb.infinitive(verb_to_match)
    elif verb_tense == 'past':
        match = verb.past(verb_to_match)
    elif verb_tense == 'present participle':
        match = verb.present_participle(verb_to_match)
    elif verb_tense == 'past participle':
        match = verb.past_participle(verb_to_match)
    elif verb_tense in present_tenses:
        tense_value = present_tenses.index(verb_tense) + 1
        match = verb.present(verb_to_match, person=tense_value, negate=False)
    elif verb_tense in past_tenses:
        tense_value = past_tenses.index(verb_tense) + 1
        match = verb.past(verb_to_match, person=tense_value, negate=False)
    else:
        match = verb.present(verb_to_match)

    return match


def load_and_parse_facts(filename):
    print("Inside load_and_parse_facts ++++++++")
    with open(filename, 'rb') as fact_file:
        for index, fact in enumerate(fact_file):
            generated_question = GeneratedQuestion(fact)
            generated_question.get_tree()
            generated_question.traverse_and_chunk()
            generated_question.apply_rules()
            write_questions_and_answers(index + 1, generated_question.fact, generated_question.question_list,
                                        generated_question.answer_list)


if __name__ == '__main__':
    # loadCorpus("b2b-lo1-corpus.dat")
    print("Inside main ++++++++")
    #pdb.set_trace()
    load_and_parse_facts('sentences.txt')
