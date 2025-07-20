Aj='All files'
Ai='*.json'
Ah='JSON files'
Ag='WM_DELETE_WINDOW'
Af=Exception
Ae=enumerate
Ac='descriptionLanguage'
Ab='vocabularyLanguage'
Aa=sorted
AY='vertical'
AX='10'
AW='Word'
AV='Index'
AU='language_conflict_msg'
AT='language_conflict_title'
AS='add_new_entry'
AR='readonly'
AQ='ui_language'
AP='file_saved_successfully'
AO='save_success_title'
AN='file_loaded_successfully'
AM='load_success_title'
AL='file_load_error'
AK='file_not_found'
AJ='json_parse_error'
AI='entry_deleted'
AH='delete_success_title'
AG='confirm_delete_msg'
AF='confirm_delete_title'
AE='select_entry_first'
AD='delete_entry_title'
AC='new_entry_added'
AB='add_success_title'
AA='index_already_exists'
A9='invalid_new_entry_index'
A8='original_entry_missing_index'
A7='entry_updated'
A6='update_success_title'
A5='no_entry_data_found'
A4='selection_error_title'
A3='cancel_metadata_msg'
A2='cancel_metadata_title'
A1='unknown_author_default'
A0='new_vocab_name_default'
z='desc_lang_iso'
y='vocab_lang_iso'
x='vocab_description'
w='vocab_author'
v='vocab_name'
u='edit_metadata_title'
t='missing_metadata_msg'
s='missing_metadata_title'
r='exit_confirm_msg'
q='exit_confirm_title'
p='delete_entry'
o='update_entry'
n='confusable_words'
m='explanation'
l='word_kanji'
k='word_kana'
j='edit_entry'
i='vocab_list'
h='explanation_lang'
g='vocab_lang'
f='language_settings'
e='save_as'
d='open'
c='file_operations'
b=int
a=list
Z='5'
Y='no_data_to_save'
X='save_file_title'
W='error_title'
V='file_error_title'
U='add_failed_title'
T='invalid_selected_index'
S='update_failed_title'
R='word_general'
Q='index'
P='save'
O='日本語'
N='English'
M=str
L='metadata'
K='app_title'
J='1.0'
I='i'
H=False
G=True
F=None
D=''
import tkinter as B
from tkinter import ttk as C,filedialog as Ad,messagebox as E
import json as AZ,re
class Ak:
	def __init__(A,master):Ao='Delete Entry';An="檔案已成功儲存到 '{0}'。";Am="檔案 '{0}' 已成功載入。";Al='載入檔案時發生錯誤: {0}';Ak='檔案未找到。';Aj='無法解析JSON檔案。請確保檔案格式正確。';Ai='詞條已刪除。';Ah='新詞條已新增。';Af='原詞條缺少索引資訊。';Ae='詞條已更新。';Ad='解釋語言 (ISO 639-1):';Ac='詞彙語言 (ISO 639-1):';Ab='詞彙表描述:';Aa='詞彙表作者:';AZ='詞彙表名稱:';AY='易混詞 (每行一個):';AX='詞彙 - 日語 Kanji 形式:';AW='詞彙 - 假名形式:';AV='MemoWord 詞彙表編輯器';AR='詞彙語言和解釋語言不能相同。';b='語言衝突';a='删除词条';Z='新增成功';M='更新成功';J='未知作者';I='索引:';G='刪除詞條';E='add_new_entry_msg';D='index_must_be_int';C='input_error_title';A.master=master;A.master.geometry('1000x700');A.data=[];A.metadata=F;A.current_file_path=F;A.selected_entry_id=F;A.unsaved_changes=H;A.LANG_TO_ISO={'中文 (简体)':'zh-Hans',N:'en',O:'ja','Français':'fr','Español':'es','Deutsch':'de','한국어':'ko','Português':'pt','Italiano':'it','Русский':'ru','العربية':'ar','हिन्दी':'hi','বাংলা':'bn','اردو':'ur','Bahasa Indonesia':'id','Türkçe':'tr','Tiếng Việt':'vi','ไทย':'th','Polski':'pl','Nederlands':'nl','Svenska':'sv','Norsk':'no','Dansk':'da','Suomi':'fi','Ελληνικά':'el','עברית':'he','فارسی':'fa','Română':'ro','Magyar':'hu','Čeština':'cs','Slovenčina':'sk','Українська':'uk','Български':'bg','Hrvatski':'hr','Srpski':'sr','Català':'ca','Eesti':'et','Latviešu':'lv','Lietuvių':'lt','Slovenščina':'sl','Afrikaans':'af','Shqip':'sq','Amharic':'am','Azərbaycan dili':'az','Беларуская':'be','Bosanski':'bs','ქართული':'ka','Kurdî':'ku','ລາວ':'lo','Македонски':'mk','Монгол':'mn','नेपाली':'ne','Oʻzbek':'uz','ਪੰਜਾਬੀ':'pa','සිංහල':'si','Sunda':'su','Kiswahili':'sw','Tagalog':'tl','தமிழ்':'ta','తెలుగు':'te','Ўзбек':'uz','Zulu':'zu'};A.ISO_TO_LANG={B:A for(A,B)in A.LANG_TO_ISO.items()};A.translations={'简体中文':{K:'MemoWord 词汇表编辑器',c:'文件操作',d:'打开',P:'保存',e:'另存为',L:'元数据',f:'语言设置',g:'词汇语言:',h:'解释语言:',i:'词汇列表',j:'编辑词条',Q:I,k:'词汇 - 假名形式:',l:'词汇 - 日语 Kanji 形式:',R:'词汇:',m:'解释:',n:'易混词 (每行一个):',AS:'新增词条',o:'更新词条',p:a,q:'退出确认',r:'您有未保存的更改。是否要保存？',s:'缺少元数据',t:'此文件缺少元数据。是否现在填写？\n(推荐填写，否则将以空元数据保存)',u:'编辑元数据',v:'词汇表名称:',w:'词汇表作者:',x:'词汇表描述:',y:'词汇语言 (ISO 639-1):',z:'解释语言 (ISO 639-1):',A0:'新词汇表',A1:J,A2:'取消元数据',A3:'您尚未保存元数据。是否确定不保存并退出？\n(这将导致文件保存失败或元数据为空)',C:'输入错误',D:'索引必须是整数。',A4:'选择错误',A5:'无法找到对应的词条数据。',E:'已清空表单，请填写新词条信息。新词条索引为 {0}。',A6:M,A7:'词条已更新。',S:'更新失败',A8:'原词条缺少索引信息。',T:'选择的词条索引无效。',U:'新增失败',A9:'无法获取新词条的有效索引。',AA:'索引 {0} 已存在，请使用不同的索引或选择现有词条进行更新。',AB:Z,AC:'新词条已新增。',AD:a,AE:'请先从列表中选择一个词条。',AF:'确认删除',AG:'您确定要删除此词条吗？',AH:'删除成功',AI:'词条已删除。',V:'文件错误',AJ:'无法解析JSON文件。请确保文件格式正确。',AK:'文件未找到。',W:'错误',AL:'加载文件时发生错误: {0}',AM:'加载成功',AN:"文件 '{0}' 已成功加载。",X:'保存文件',Y:'没有数据可供保存。',AO:'保存成功',AP:"文件已成功保存到 '{0}'。",AQ:'界面語言:',AT:b,AU:AR},'繁體中文':{K:AV,c:'檔案操作',d:'開啟',P:'儲存',e:'另存為',L:'元數據',f:'語言設定',g:'詞彙語言:',h:'解釋語言:',i:'詞彙列表',j:'編輯詞條',Q:I,k:AW,l:AX,R:'詞彙:',m:'解釋:',n:AY,AS:'新增詞條',o:'更新詞條',p:G,q:'退出確認',r:'您有未儲存的更改。是否要儲存？',s:'缺少元數據',t:'此檔案缺少元數據。是否現在填寫？\n(推薦填寫，否則將以空元數據儲存)',u:'編輯元數據',v:AZ,w:Aa,x:Ab,y:Ac,z:Ad,A0:'新詞彙表',A1:J,A2:'取消元數據',A3:'您尚未儲存元數據。是否確定不儲存並退出？\n(這將導致檔案儲存失敗或元數據為空)',C:'輸入錯誤',D:'索引必須是整數。',A4:'選擇錯誤',A5:'無法找到對應的詞條資料。',E:'已清空表單，請填寫新詞條資訊。新詞條索引為 {0}。',A6:M,A7:Ae,S:'更新失敗',A8:Af,T:'選擇的詞條索引無效。',U:'新增失敗',A9:'無法取得新詞條的有效索引。',AA:'索引 {0} 已存在，請使用不同的索引或選擇現有詞條進行更新。',AB:Z,AC:Ah,AD:G,AE:'請先從列表中選擇一個詞條。',AF:'確認刪除',AG:'您確定要刪除此詞條嗎？',AH:'刪除成功',AI:Ai,V:'檔案錯誤',AJ:Aj,AK:Ak,W:'錯誤',AL:Al,AM:'載入成功',AN:Am,X:'儲存檔案',Y:'沒有資料可供儲存。',AO:'儲存成功',AP:An,AQ:'介面語言:',AT:b,AU:AR},'粵語':{K:AV,c:'檔案操作',d:'開啟',P:'儲存',e:'另存為',L:'元數據',f:'語言設定',g:'詞彙語言:',h:'解釋語言:',i:'詞彙列表',j:'編輯詞條',Q:I,k:AW,l:AX,R:'詞彙:',m:'解釋:',n:AY,o:'更新詞條',p:G,q:'退出確認',r:'您有未儲存嘅更改。係咪要儲存？',s:'缺少元數據',t:'呢個檔案缺少元數據。而家填寫？\n(建議填寫，否則會以空元數據儲存)',u:'編輯元數據',v:AZ,w:Aa,x:Ab,y:Ac,z:Ad,A0:'新詞彙表',A1:J,A2:'取消元數據',A3:'您仲未儲存元數據。係咪確定唔儲存就離開？\n(咁會導致檔案儲存失敗或者元數據係空嘅)',C:'輸入錯誤',D:'索引必須係整數。',A4:'選擇錯誤',A5:'搵唔到對應嘅詞條資料。',E:'已清空表單，請填寫新詞條資訊。新詞條索引係 {0}。',A6:M,A7:Ae,S:'更新失敗',A8:Af,T:'選擇嘅詞條索引無效。',U:'新增失敗',A9:'攞唔到新詞條嘅有效索引。',AA:'索引 {0} 已存在，請使用唔同嘅索引或者選擇現有詞條更新。',AB:Z,AC:Ah,AD:G,AE:'請先喺列表揀一個詞條。',AF:'確認刪除',AG:'您確定要刪除呢個詞條嗎？',AH:'刪除成功',AI:Ai,V:'檔案錯誤',AJ:Aj,AK:Ak,W:'錯誤',AL:Al,AM:'載入成功',AN:Am,X:'儲存檔案',Y:'冇資料可以儲存。',AO:'儲存成功',AP:An,AQ:'介面語言:'},N:{K:'MemoWord Vocabulary Editor',c:'File Operations',d:'Open',P:'Save',e:'Save As',L:'Metadata',f:'Language Settings',g:'Vocabulary Language:',h:'Explanation Language:',i:'Vocabulary List',j:'Edit Entry',Q:'Index:',k:'Word - Kana Form:',l:'Word - Kanji Form:',R:'Word:',m:'Explanation:',n:'Confusable Words (one per line):',AS:'Add New Entry',o:'Update Entry',p:Ao,q:'Exit Confirmation',r:'You have unsaved changes. Do you want to save?',s:'Missing Metadata',t:'This file is missing metadata. Do you want to fill it in now?\n(Recommended, otherwise it will be saved with empty metadata)',u:'Edit Metadata',v:'Vocabulary Name:',w:'Vocabulary Author:',x:'Vocabulary Description:',y:'Vocabulary Language (ISO 639-1):',z:'Explanation Language (ISO 639-1):',A0:'New Vocabulary',A1:'Unknown Author',A2:'Cancel Metadata',A3:'You have not saved metadata. Are you sure you want to exit without saving?\n(This will cause file save to fail or metadata to be empty)',C:'Input Error',D:'Index must be an integer.',A4:'Selection Error',A5:'Could not find corresponding entry data.',E:'Form cleared. Please fill in new entry information. New entry index is {0}.',A6:'Update Successful',A7:'Entry updated.',S:'Update Failed',A8:'Original entry is missing index information.',T:'Selected entry index is invalid.',U:'Add Failed',A9:'Could not get a valid index for the new entry.',AA:'Index {0} already exists. Please use a different index or select an existing entry to update.',AB:'Add Successful',AC:'New entry added.',AD:Ao,AE:'Please select an entry from the list first.',AF:'Confirm Deletion',AG:'Are you sure you want to delete this entry?',AH:'Delete Successful',AI:'Entry deleted.',V:'File Error',AJ:'Could not parse JSON file. Please ensure the file format is correct.',AK:'File not found.',W:'Error',AL:'An error occurred while loading the file: {0}',AM:'Load Successful',AN:"File '{0}' loaded successfully.",X:'Save File',Y:'No data to save.',AO:'Save Successful',AP:"File successfully saved to '{0}'.",AQ:'UI Language:'}};A.ui_language_var=B.StringVar(value=N);A.current_ui_language=A.ui_language_var.get();A._create_widgets();A._set_ui_language();A.vocab_lang_var.set(N);A.explanation_lang_var.set(O);A._update_treeview();A._add_new_entry_mode();A.master.protocol(Ag,A._on_closing)
	def _translate(A,key,*B):C=A.translations.get(A.current_ui_language,{}).get(key,key);return C.format(*B)if B else C
	def _set_ui_language(A,event=F):A.current_ui_language=A.ui_language_var.get();A.master.title(A._translate(K));A.file_buttons_frame.config(text=A._translate(c));A.open_button.config(text=A._translate(d));A.save_button.config(text=A._translate(P));A.save_as_button.config(text=A._translate(e));A.metadata_button.config(text=A._translate(L));A.language_frame.config(text=A._translate(f));A.vocab_lang_label.config(text=A._translate(g));A.explanation_lang_label.config(text=A._translate(h));A.ui_lang_label.config(text=A._translate(AQ));A.list_frame.config(text=A._translate(i));A.tree.heading(AV,text=A._translate(Q));A.tree.heading(AW,text=A._translate(R));A.edit_frame.config(text=A._translate(j));A.index_label_text.set(A._translate(Q));A.explanation_label.config(text=A._translate(m));A.confusable_words_label.config(text=A._translate(n));A.update_button.config(text=A._translate(o));A.delete_button.config(text=A._translate(p));A.add_new_entry_button.config(text=A._translate(AS));A._on_vocabulary_language_change()
	def _create_widgets(A):I='<<ComboboxSelected>>';F=C.Frame(A.master,padding=AX);F.pack(fill=B.X);A.file_buttons_frame=C.LabelFrame(F,text=D,padding=Z);A.file_buttons_frame.pack(side=B.LEFT,padx=10,pady=5);A.open_button=C.Button(A.file_buttons_frame,text=D,command=A._open_file_dialog);A.open_button.pack(side=B.LEFT,padx=5);A.save_button=C.Button(A.file_buttons_frame,text=D,command=A._save_file_dialog);A.save_button.pack(side=B.LEFT,padx=5);A.save_as_button=C.Button(A.file_buttons_frame,text=D,command=A._save_as_file_dialog);A.save_as_button.pack(side=B.LEFT,padx=5);A.metadata_button=C.Button(A.file_buttons_frame,text=D,command=A._open_metadata_dialog);A.metadata_button.pack(side=B.LEFT,padx=5);J=Aa(a(A.LANG_TO_ISO.keys()));A.language_frame=C.LabelFrame(F,text=D,padding=Z);A.language_frame.pack(side=B.LEFT,padx=10,pady=5);A.vocab_lang_label=C.Label(A.language_frame,text=D);A.vocab_lang_label.pack(side=B.LEFT,padx=5);A.vocab_lang_var=B.StringVar(value=N);A.vocab_lang_combobox=C.Combobox(A.language_frame,textvariable=A.vocab_lang_var,values=J,state=AR);A.vocab_lang_combobox.pack(side=B.LEFT,padx=5);A.vocab_lang_combobox.bind(I,A._on_vocabulary_language_change);A.explanation_lang_label=C.Label(A.language_frame,text=D);A.explanation_lang_label.pack(side=B.LEFT,padx=5);A.explanation_lang_var=B.StringVar(value=O);A.explanation_lang_combobox=C.Combobox(A.language_frame,textvariable=A.explanation_lang_var,values=J,state=AR);A.explanation_lang_combobox.pack(side=B.LEFT,padx=5);A.explanation_lang_combobox.bind(I,A._on_explanation_language_change);H=C.Frame(A.master,padding=AX);H.pack(fill=B.BOTH,expand=G);A.list_frame=C.LabelFrame(H,text=D,padding=Z);A.list_frame.pack(side=B.LEFT,fill=B.BOTH,expand=G,padx=(0,10));A.tree=C.Treeview(A.list_frame,columns=(AV,AW),show='headings');A.tree.heading(AV,text=D);A.tree.heading(AW,text=D);A.tree.column(AV,width=50,stretch=B.NO);A.tree.column(AW,width=250,stretch=B.YES);A.tree.pack(side=B.LEFT,fill=B.BOTH,expand=G);K=C.Scrollbar(A.list_frame,orient=AY,command=A.tree.yview);K.pack(side=B.RIGHT,fill=B.Y);A.tree.configure(yscrollcommand=K.set);A.tree.bind('<<TreeviewSelect>>',A._on_treeview_select);A.tree.bind('<Button-1>',A._on_treeview_click);A.edit_frame=C.LabelFrame(H,text=D,padding=AX);A.edit_frame.pack(side=B.RIGHT,fill=B.BOTH,expand=G);A.index_label_text=B.StringVar(value=D);C.Label(A.edit_frame,textvariable=A.index_label_text).grid(row=0,column=0,sticky=B.W,pady=2);A.i_var=B.StringVar();A.i_label=C.Label(A.edit_frame,textvariable=A.i_var);A.i_label.grid(row=0,column=1,sticky=(B.W,B.E),pady=2);A.w_main_label_text=B.StringVar(value=D);C.Label(A.edit_frame,textvariable=A.w_main_label_text).grid(row=1,column=0,sticky=B.W,pady=2);A.w_kana_entry=C.Entry(A.edit_frame,width=40);A.w_kana_entry.grid(row=1,column=1,sticky=(B.W,B.E),pady=2);A.w_kanji_label_text=B.StringVar(value=D);A.kanji_label=C.Label(A.edit_frame,textvariable=A.w_kanji_label_text);A.kanji_label.grid(row=2,column=0,sticky=B.W,pady=2);A.w_kanji_entry=C.Entry(A.edit_frame,width=40);A.w_kanji_entry.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);A.explanation_label=C.Label(A.edit_frame,text=D);A.explanation_label.grid(row=3,column=0,sticky=B.W,pady=2);A.d_text=B.Text(A.edit_frame,height=5,width=40,wrap=B.WORD);A.d_text.grid(row=3,column=1,sticky=(B.W,B.E),pady=2);L=C.Scrollbar(A.edit_frame,orient=AY,command=A.d_text.yview);L.grid(row=3,column=2,sticky=B.NS);A.d_text.configure(yscrollcommand=L.set);A.confusable_words_label=C.Label(A.edit_frame,text=D);A.confusable_words_label.grid(row=4,column=0,sticky=B.W,pady=2);A.o_text=B.Text(A.edit_frame,height=5,width=40,wrap=B.WORD);A.o_text.grid(row=4,column=1,sticky=(B.W,B.E),pady=2);M=C.Scrollbar(A.edit_frame,orient=AY,command=A.o_text.yview);M.grid(row=4,column=2,sticky=B.NS);A.o_text.configure(yscrollcommand=M.set);E=C.Frame(A.edit_frame,padding=Z);E.grid(row=5,column=0,columnspan=3,pady=10);A.add_new_entry_button=C.Button(E,text=D,command=A._add_new_entry_mode);A.add_new_entry_button.pack(side=B.LEFT,padx=5);A.add_new_entry_button.pack_forget();A.update_button=C.Button(E,text=D,command=A._update_entry);A.update_button.pack(side=B.LEFT,padx=5);A.delete_button=C.Button(E,text=D,command=A._delete_entry);A.delete_button.pack(side=B.LEFT,padx=5);A.edit_frame.grid_columnconfigure(1,weight=1);A.edit_frame.grid_rowconfigure(3,weight=1);A.edit_frame.grid_rowconfigure(4,weight=1);A.bottom_right_frame=C.Frame(A.master,padding=Z);A.bottom_right_frame.pack(side=B.BOTTOM,anchor=B.SE,padx=10,pady=5);A.ui_lang_label=C.Label(A.bottom_right_frame,text=D);A.ui_lang_label.pack(side=B.LEFT,padx=5);A.ui_language_combobox=C.Combobox(A.bottom_right_frame,textvariable=A.ui_language_var,values=['简体中文','繁體中文','粵語',N],state=AR,width=15);A.ui_language_combobox.pack(side=B.LEFT,padx=5);A.ui_language_combobox.bind(I,A._set_ui_language)
	def _update_treeview(A):
		for E in A.tree.get_children():A.tree.delete(E)
		for(F,C)in Ae(A.data):G=C.get(I,D);H=C.get('w',D);A.tree.insert(D,B.END,iid=M(F),values=(G,H))
	def _clear_entry_form(A):A.i_var.set(D);A.w_kana_entry.delete(0,B.END);A.w_kanji_entry.delete(0,B.END);A.d_text.delete(J,B.END);A.o_text.delete(J,B.END);A.selected_entry_id=F;A.add_new_entry_button.pack_forget()
	def _populate_entry_form(A,entry_data):
		C=entry_data;A._clear_entry_form();A.i_var.set(M(C.get(I,D)));F=C.get('w',D)
		if A.vocab_lang_var.get()==O:
			E=re.match('^(.*?)(?:〔(.*?)〕)?$',F)
			if E:G=E.group(1);H=E.group(2)if E.group(2)else D;A.w_kana_entry.insert(0,G);A.w_kanji_entry.insert(0,H)
			else:A.w_kana_entry.insert(0,F)
		else:A.w_kana_entry.insert(0,F)
		A.d_text.insert(J,C.get('d',D));K=C.get('o',[]);A.o_text.insert(J,'\n'.join(K));A.add_new_entry_button.pack(side=B.LEFT,padx=5)
	def _get_form_data(A):
		E=A.w_kana_entry.get().strip();F=A.w_kanji_entry.get().strip();C=D
		if A.vocab_lang_var.get()==O and F:C=f"{E}〔{F}〕"
		else:C=E
		G=A.d_text.get(J,B.END).strip();H=A.o_text.get(J,B.END).strip();I=[A.strip()for A in H.split('\n')if A.strip()];return{'w':C,'d':G,'o':I}
	def _on_treeview_select(A,event):
		B=A.tree.selection()
		if not B:return
		A.selected_entry_id=B[0];C=b(A.selected_entry_id)
		if 0<=C<len(A.data):A._populate_entry_form(A.data[C])
		else:A._clear_entry_form();E.showwarning(A._translate(A4),A._translate(A5))
	def _on_treeview_click(A,event):
		B=A.tree.identify_row(event.y)
		if B:0
		else:A.tree.selection_remove(A.tree.selection());A._add_new_entry_mode()
	def _add_new_entry_mode(A):
		A._clear_entry_form();B=0
		if A.data:
			C=[A.get(I,-1)for A in A.data]
			if C:B=max(C)+1
			else:B=0
		A.i_var.set(M(B));A.selected_entry_id=F;A.unsaved_changes=G;A.add_new_entry_button.pack_forget()
	def _update_entry(A):
		D=A._get_form_data()
		if D is F:return
		B=F
		if A.selected_entry_id is not F:
			H=b(A.selected_entry_id)
			if 0<=H<len(A.data):
				J=A.data[H].get(I)
				if J is F:E.showerror(A._translate(S),A._translate(A8));return
				L={**D,I:J};A.data[H]=L;B=J;E.showinfo(A._translate(A6),A._translate(A7))
			else:E.showerror(A._translate(S),A._translate(T));return
		else:
			try:C=b(A.i_var.get())
			except ValueError:E.showerror(A._translate(U),A._translate(A9));return
			N={A[I]for A in A.data if I in A}
			if C in N:E.showerror(A._translate(U),A._translate(AA,C));return
			O={**D,I:C};A.data.append(O);A.data.sort(key=lambda x:x.get(I,float('inf')));B=C;E.showinfo(A._translate(AB),A._translate(AC))
		A._update_treeview()
		if B is not F:
			for(K,P)in Ae(A.data):
				if P.get(I)==B:A.tree.selection_set(M(K));A.tree.focus(M(K));A.selected_entry_id=M(K);break
		A.unsaved_changes=G
	def _delete_entry(A):
		if A.selected_entry_id is F:E.showwarning(A._translate(AD),A._translate(AE));return
		C=E.askyesno(A._translate(AF),A._translate(AG))
		if C:
			B=b(A.selected_entry_id)
			if 0<=B<len(A.data):del A.data[B];A._update_treeview();A._add_new_entry_mode();E.showinfo(A._translate(AH),A._translate(AI));A.unsaved_changes=G
			else:E.showerror(A._translate('delete_failed_title'),A._translate(T))
	def _open_file_dialog(B):
		A=Ad.askopenfilename(defaultextension='.json',filetypes=[(Ah,Ai),(Aj,'*.*')])
		if A:B._load_json(A)
	def _load_json(A,file_path):
		C=file_path
		try:
			with open(C,'r',encoding='utf-8')as D:B=AZ.load(D)
			A.data=[];A.metadata=F
			if B and isinstance(B,a)and B[0].get(L)is G:A.metadata=B.pop(0);A.data=B
			else:A.data=B
			A.current_file_path=C;A.master.title(f"{A._translate(K)} - {C}");A._update_treeview();A._clear_entry_form();A._add_new_entry_mode();A.unsaved_changes=H;E.showinfo(A._translate(AM),A._translate(AN,C))
		except AZ.JSONDecodeError:E.showerror(A._translate(V),A._translate(AJ))
		except FileNotFoundError:E.showerror(A._translate(V),A._translate(AK))
		except Af as I:E.showerror(A._translate(W),A._translate(AL,I))
	def _save_file_dialog(A):
		if not A.data and not A.metadata:E.showwarning(A._translate(X),A._translate(Y));return H
		if A.current_file_path:return A._save_json(A.current_file_path)
		else:return A._save_as_file_dialog()
	def _save_as_file_dialog(A):
		if not A.data and not A.metadata:E.showwarning(A._translate(X),A._translate(Y));return H
		B=Ad.asksaveasfilename(defaultextension='.json',filetypes=[(Ah,Ai),(Aj,'*.*')])
		if B:return A._save_json(B)
		return H
	def _save_json(A,file_path):
		B=file_path
		if A.metadata is F:
			J=E.askyesno(A._translate(s),A._translate(t))
			if J:
				if not A._open_metadata_dialog(force_save=G):return H
		try:
			C=a(A.data)
			if A.metadata:
				if A.vocab_lang_var.get()and A.explanation_lang_var.get():A.metadata[Ab]=A.LANG_TO_ISO.get(A.vocab_lang_var.get(),D);A.metadata[Ac]=A.LANG_TO_ISO.get(A.explanation_lang_var.get(),D)
				C.insert(0,A.metadata)
			C[1:].sort(key=lambda x:x.get(I,float('inf')))
			with open(B,'w',encoding='utf-8')as L:AZ.dump(C,L,ensure_ascii=H,indent=4)
			A.current_file_path=B;A.master.title(f"{A._translate(K)} - {B}");A.unsaved_changes=H;E.showinfo(A._translate(AO),A._translate(AP,B));return G
		except Af as M:E.showerror(A._translate(W),A._translate('file_save_error',M));return H
	def _check_language_conflict(A):
		B=A.vocab_lang_var.get();C=A.explanation_lang_var.get()
		if B and C and B==C:E.showwarning(A._translate(AT),A._translate(AU));return G
		return H
	def _on_vocabulary_language_change(A,event=F):
		G=A.vocab_lang_var.get()
		if A._check_language_conflict():0
		E=A.vocab_lang_var.get()
		if E==O:A.w_main_label_text.set(A._translate(k));A.w_kanji_label_text.set(A._translate(l));A.kanji_label.grid(row=2,column=0,sticky=B.W,pady=2);A.w_kanji_entry.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);A.w_kana_entry.config(state=B.NORMAL)
		else:A.w_main_label_text.set(A._translate(R));A.w_kanji_label_text.set(D);A.kanji_label.grid_forget();A.w_kanji_entry.grid_forget();A.w_kanji_entry.delete(0,B.END);A.w_kana_entry.config(state=B.NORMAL)
		if A.selected_entry_id is not F:
			C=b(A.selected_entry_id)
			if 0<=C<len(A.data):A._populate_entry_form(A.data[C])
	def _on_explanation_language_change(A,event=F):
		B=A.explanation_lang_var.get()
		if A._check_language_conflict():0
	def _on_closing(A):
		if A.unsaved_changes:B=E.askyesnocancel(A._translate(q),A._translate(r))
		else:A.master.destroy()
	def _open_metadata_dialog(A,force_save=H):
		W='description';V='author';U='name';F=B.Toplevel(A.master);F.title(A._translate(u));F.transient(A.master);F.grab_set();F.geometry('400x300');I=C.Frame(F,padding=AX);I.pack(fill=B.BOTH,expand=G);C.Label(I,text=A._translate(v)).grid(row=0,column=0,sticky=B.W,pady=2);O=B.StringVar();X=C.Entry(I,textvariable=O,width=40);X.grid(row=0,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(w)).grid(row=1,column=0,sticky=B.W,pady=2);Q=B.StringVar();Y=C.Entry(I,textvariable=Q,width=40);Y.grid(row=1,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(x)).grid(row=2,column=0,sticky=B.W,pady=2);K=B.Text(I,height=5,width=40,wrap=B.WORD);K.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);S=C.Scrollbar(I,orient=AY,command=K.yview);S.grid(row=2,column=2,sticky=B.NS);K.configure(yscrollcommand=S.set);C.Label(I,text=A._translate(y)).grid(row=3,column=0,sticky=B.W,pady=2);M=B.StringVar();b=C.Combobox(I,textvariable=M,values=Aa(a(A.ISO_TO_LANG.keys())),state=AR,width=37);b.grid(row=3,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(z)).grid(row=4,column=0,sticky=B.W,pady=2);N=B.StringVar();c=C.Combobox(I,textvariable=N,values=Aa(a(A.ISO_TO_LANG.keys())),state=AR,width=37);c.grid(row=4,column=1,sticky=(B.W,B.E),pady=2)
		if A.metadata:O.set(A.metadata.get(U,D));Q.set(A.metadata.get(V,D));K.insert(J,A.metadata.get(W,D));M.set(A.metadata.get(Ab,D));N.set(A.metadata.get(Ac,D))
		else:O.set(A._translate(A0));Q.set(A._translate(A1));M.set(A.LANG_TO_ISO.get(A.vocab_lang_var.get(),D));N.set(A.LANG_TO_ISO.get(A.explanation_lang_var.get(),D))
		def d():
			if M.get()==N.get():E.showwarning(A._translate(AT),A._translate(AU));return
			A.metadata={L:G,U:O.get().strip(),V:Q.get().strip(),W:K.get(J,B.END).strip(),Ab:M.get().strip(),Ac:N.get().strip()};A.unsaved_changes=G;F.destroy()
		def T():
			if force_save:
				B=E.askyesno(A._translate(A2),A._translate(A3))
				if B:F.destroy();F.result=H
			else:F.destroy();F.result=H
		R=C.Frame(I,padding=Z);R.grid(row=5,column=0,columnspan=3,pady=10);C.Button(R,text=A._translate(P),command=d).pack(side=B.LEFT,padx=5);C.Button(R,text=A._translate('cancel_metadata'),command=T).pack(side=B.LEFT,padx=5);F.protocol(Ag,T);A.master.wait_window(F);return getattr(F,'result',G)
if __name__=='__main__':A=B.Tk();Al=Ak(A);A.mainloop()