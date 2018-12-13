from lxml import etree
from io import StringIO, BytesIO

		
def FileTXTProcess(pFile, AgencyName, CiteNumber, lnlni, lnsmi, buf,ProjCode):
    #string OpenFile = "";
    buf = ""
    CiteNumber = ""
    AgencyName = ""
    lnlni = ""
    lnsmi = ""
    string MoveFolder = ""
    highlight_text=[]
    #MoveFolder = Path.GetDirectoryName(pFile) + "\\MoveCompletedFiles";
    try:
        buf =BeautifulSoup(open("D:\\YK Python\\xmltodict\\LUMNLRB3.BL23898910.xml","r"))
        mc = buf.find("case_cite" or "lnv:cite")
        if mc:
            if mc.text.find("LEXIS") > -1:
                CiteNumber = mc.text.split(';')[0]
            else:
                mc = mc.find("cite")
                #mc = re.match("<cite>([^<]*) LEXIS ([^<]*)</cite>", mc)
                if mc:
                    buf = re.sub(r"<cite>([^<]*) LEXIS ([^<]*)</cite>", "@@@citeNumber###$1 LEXIS $2@@@/citeNumber###", buf)
                    CiteNumber = mc.text
                    CiteNumber = re.sub(r"<([^>]*)>", "", CiteNumber)
                    CiteNumber = re.sub(r";$", "", CiteNumber).strip()
                        

        #lnlni = re.match("<lndocmeta:lnlni ([^>]*)lnlni=\"([^\"]*)\"([^>]*)>", buf)
        lnlni = buf.find("lndocmeta:lnlni").text
        lnsmi = buf.find("lndocmeta:smi").text

        mc = buf.find("lnv:agency")
        if mc:
            AgencyName = mc.text
            #AgencyNamematch = re.match("<([^>]*)>", AgencyName)
            AgencyName = re.sub(r"<([^>]*)>","", AgencyName)
            #AgencyName = AgencyName.Replace("<agency>", "").Replace("</agency>", "").Trim();
                

                   
        lnv_opinion= buf.find("<lnv:OPINION ") or buf.find("<lnv:OPINION>") or buf.find("<lnv:OPINION-1") or buf.find("<lnv:ALJ-DECISION segformat") or buf.find("<OPINION>") or buf.find("<ALJ_DECISION>")
        if lnv_opinion:
            highlight_text.append(lnv_opinion.text)
        #buf = Regex.Replace(buf, "<p><emph ([^>]*)>", "@@@Heading###");
        #buf = re.sub(r"&amp;([a-z]+)", "&$1", buf)
        #buf = buf.replace("<lnvxe:footnote>", "@@@FootnoteStart###<lnvxe:footnote>").replace("<lnvxe:footnote ", "@@@FootnoteStart###<lnvxe:footnote ").replace("</lnvxe:footnote>", "@@@FootnoteEnd###")
        lnv_footnote= buf.find("<lnvxe:footnote>") or buf.find("<lnvxe:footnote ")

        #buf = buf.Replace("<lnvxe:footnote>", "@@@FootnoteStart###<lnvxe:footnote>").Replace("<lnvxe:footnote ", "@@@FootnoteStart###<lnvxe:footnote ").Replace("</lnvxe:footnote>", "@@@FootnoteEnd###");
        #if (ProjCode == "OP-LN-0516" || ProjCode == "PB-AGNY-1054")
             
        #    buf = re.sub(r">([^<]*)</lnvxe:fnlabel>", ">", buf)
        #    buf = re.sub("<([^>]*)>", "", buf)

        #buf = buf.replace("@@@HighlightStart###", "\r\n<HIGHLIGHT>").replace("@@@HighlightEnd###", "\r\n</HIGHLIGHT>").replace("@@@Heading###", "\r\n<H>")
        #buf = buf.replace("@@@FootnoteStart###", "\r\n<FT>").replace("@@@FootnoteEnd###", "\r\n</FT>\r\n")
        #buf = buf.replace("@@@full_namestart###", "\r\n<full_name>").replace("@@@full_nameend###", "</full_name>\r\n")
        #buf = buf.replace("@@@agencystart###", "\r\n<agency>").replace("@@@agencyend###", "</agency>\r\n")
        #buf = buf.replace("@@@CaseStart###", "<CASE>").replace("@@@CaseEnd###", "</CASE>").replace(".</CASE>", "</CASE>.")
        #buf = buf.replace("@@@citeNumber###", "<citeNumber>").replace("@@@/citeNumber###", "</citeNumber>")
        #buf = buf.strip(' ')
        #buf = buf.replace("&amp;#", "&#")
        #Entity_Convert.EntityConvert ObjEnt = new Entity_Convert.EntityConvert();
        #buf = ObjEnt.entity_enterchange(buf, "HEXA");
        #buf = ObjEnt.utf_conversion(buf.Replace("&#x0027;", "'"))
		
    def Doing_HighLight_Text():
        KeywordInJudgement = ""
        statutes = ""
        first_para = ""
        htmlText = ""
        HWindowHtml = ""
        HWebHtml = ""
        