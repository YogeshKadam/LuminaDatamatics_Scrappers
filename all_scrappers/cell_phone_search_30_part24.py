


import pandas as pd



excel_file=pd.ExcelFile(r'D:\YK Python\Cell_phone\Cell Phone Cases_14_Attribute_new_3.xlsx')


df1 = pd.read_excel(excel_file, 'Data', skiprows=574999, skip_footer= 51664)


df2 = pd.read_excel(excel_file, 'Keywords')

df1=df1.fillna('')


df2=df2.fillna('')


def get_compatible_models1(row, pn1,pn2,pn3):
    dicts = {}
    try:
        cm = row.compatible_models 
        if cm and pn1.lower().replace(' ','').find(cm.lower().replace(' ','')) > -1:
            dicts['compatible_models']=cm
        elif cm and pn2.lower().replace(' ','').find(cm.lower().replace(' ','')) > -1:
            dicts['compatible_models']=cm
        elif cm and pn3.lower().replace(' ','').find(cm.lower().replace(' ','')) > -1:
            dicts['compatible_models']=cm
    except: pass
    try:
        mod=row.model
        if mod and pn1.lower().replace(' ','').find(mod.lower().replace(' ','')) > -1:
            dicts['model']=mod
        elif mod and pn2.lower().replace(' ','').find(mod.lower().replace(' ','')) > -1:
            dicts['model']=mod
        elif mod and pn3.lower().replace(' ','').find(mod.lower().replace(' ','')) > -1:
            dicts['model']=mod
    except: pass
	
	
    try:
        cb=row.compatible_brands
        if cb and pn1.lower().replace(' ','').find(cb.lower().replace(' ','')) > -1:
            dicts['compatible_brands']=cb
        elif cb and pn2.lower().replace(' ','').find(cb.lower().replace(' ','')) > -1:
            dicts['compatible_brands']=cb
        elif cb and pn3.lower().replace(' ','').find(cb.lower().replace(' ','')) > -1:
            dicts['compatible_brands']=cb
    except: pass
	
    try:
        col=row.color
        if col and pn1.lower().replace(' ','').find(col.lower().replace(' ','')) > -1:
            dicts['color']=col
        elif col and pn2.lower().replace(' ','').find(col.lower().replace(' ','')) > -1:
            dicts['color']=col
        elif col and pn3.lower().replace(' ','').find(col.lower().replace(' ','')) > -1:
            dicts['color']=col
    except: pass
		
    try:
        mat=row.material
        if mat and pn1.lower().replace(' ','').find(mat.lower().replace(' ','')) > -1:
            dicts['material']=mat
        elif mat and pn2.lower().replace(' ','').find(mat.lower().replace(' ','')) > -1:
            dicts['material']=mat
        elif mat and pn3.lower().replace(' ','').find(mat.lower().replace(' ','')) > -1:
            dicts['material']=mat
    except: pass

    try:
        pai=row.product_accessories_included
        if pai and pn1.lower().replace(' ','').find(pai.lower().replace(' ','')) > -1:
            dicts['product_accessories_included']=pai
        elif pai and pn2.lower().replace(' ','').find(pai.lower().replace(' ','')) > -1:
            dicts['product_accessories_included']=pai
        elif pai and pn3.lower().replace(' ','').find(pai.lower().replace(' ','')) > -1:
            dicts['product_accessories_included']=pai
    except: pass
		
    try:
        cpct=row.cell_phone_case_type
        if cpct and pn1.lower().replace(' ','').find(cpct.lower().replace(' ','')) > -1:
            dicts['cell_phone_case_type']=cpct
        elif cpct and pn2.lower().replace(' ','').find(cpct.lower().replace(' ','')) > -1:
            dicts['cell_phone_case_type']=cpct
        elif cpct and pn3.lower().replace(' ','').find(cpct.lower().replace(' ','')) > -1:
            dicts['cell_phone_case_type']=cpct
    except: pass
	
    try:
        cpcf=row['Cell Phone Case Features']
        if cpcf and pn1.lower().replace(' ','').find(cpcf.lower().replace(' ','')) > -1:
            dicts['Cell Phone Case Features']=cpcf
        elif cpcf and pn2.lower().replace(' ','').find(cpcf.lower().replace(' ','')) > -1:
            dicts['Cell Phone Case Features']=cpcf
        elif cpcf and pn3.lower().replace(' ','').find(cpcf.lower().replace(' ','')) > -1:
            dicts['Cell Phone Case Features']=cpcf
    except: pass
		
    try:
        iw=row.Is_Waterproof
        if iw and pn1.lower().replace(' ','').find(iw.lower().replace(' ','')) > -1:
            dicts['Is_Waterproof']=iw
        elif iw and pn2.lower().replace(' ','').find(iw.lower().replace(' ','')) > -1:
            dicts['Is_Waterproof']=iw
        elif iw and pn3.lower().replace(' ','').find(iw.lower().replace(' ','')) > -1:
            dicts['Is_Waterproof']=iw
    except: pass

    try:
        wrd=row['Water-Resistan Depth']
        dd=row['Drop Distance']
        if wrd and pn1.lower().replace(' ','').find(wrd.replace(' ','')) > -1:
            ind=pn1.lower().replace(' ','').index('feet')
            try : size=pn1[ind-24:ind+4]
            except : size=pn1[:ind+4]
            dicts['Water-Resistan Depth']=size
            dicts['Drop Distance']=size
        elif wrd and pn2.lower().replace(' ','').find(wrd.replace(' ','')) > -1:
            ind=pn2.lower().replace(' ','').index('feet')
            try : size=pn2[ind-24:ind+4]
            except : size=pn2[:ind+4]
            dicts['Water-Resistan Depth']=size
            dicts['Drop Distance']=size
        elif wrd and pn3.lower().replace(' ','').find(wrd.replace(' ','')) > -1:
            ind=pn3.lower().replace(' ','').index('feet')
            try : size=pn3[ind-24:ind+4]
            except : size=pn3[:ind+4]
            dicts['Water-Resistan Depth']=size
            dicts['Drop Distance']=size
    except: pass
    #print dicts
    return dicts


def get_compatible_models(row):
    
    try:
        pn1=row['product_name']
        pn2=row['product_short_description']
        pn3=row['product_long_description']
		
        #df2['out'] = df2.apply(lambda row: get_compatible_models1(row, pn1,pn2,pn3), axis=1)
        #return  [ i for i in df2['out'] if i  ] 
        #list_of_dicts=[]
        df2['out'] = df2.apply(lambda row: get_compatible_models1(row, pn1,pn2,pn3), axis=1)
        return  [ i for i in df2['out'] if i  ] 

    except: pass



df1['all_results'] = df1.apply(lambda row: get_compatible_models(row), axis=1)
#print df1['compatible_models']
print
print
print df1
df1.to_excel('output_part24_25k_30.xlsx')
