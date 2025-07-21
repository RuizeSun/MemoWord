Ao='All files'
An='*.json'
Am='JSON files'
Al='WM_DELETE_WINDOW'
Ak=Exception
Aj=enumerate
Ah='descriptionLanguage'
Ag='vocabularyLanguage'
Af='Delete.TButton'
Ae=sorted
Ac='vertical'
Ab='10'
Aa='Word'
AZ='Index'
AY='language_conflict_msg'
AX='language_conflict_title'
AW='solid'
AV='ui_language'
AU='file_saved_successfully'
AT='save_success_title'
AS='file_loaded_successfully'
AR='load_success_title'
AQ='file_load_error'
AP='file_not_found'
AO='json_parse_error'
AN='entry_deleted'
AM='delete_success_title'
AL='confirm_delete_msg'
AK='confirm_delete_title'
AJ='select_entry_first'
AI='delete_entry_title'
AH='new_entry_added'
AG='add_success_title'
AF='index_already_exists'
AE='invalid_new_entry_index'
AD='original_entry_missing_index'
AC='entry_updated'
AB='update_success_title'
AA='no_entry_data_found'
A9='selection_error_title'
A8='cancel_metadata_msg'
A7='cancel_metadata_title'
A6='unknown_author_default'
A5='new_vocab_name_default'
A4='desc_lang_iso'
A3='vocab_lang_iso'
A2='vocab_description'
A1='vocab_author'
A0='vocab_name'
z='edit_metadata_title'
y='missing_metadata_msg'
x='missing_metadata_title'
w='exit_confirm_msg'
v='exit_confirm_title'
u='delete_entry'
t='update_entry'
s='add_new_entry'
r='confusable_words'
q='explanation'
p='word_kanji'
o='word_kana'
n='edit_entry'
m='vocab_list'
l='explanation_lang'
k='vocab_lang'
j='language_settings'
i='save_as'
h='open'
g='file_operations'
f=int
e=list
d='5'
c='Secondary.TButton'
b='Primary.TButton'
a='no_data_to_save'
Z='save_file_title'
Y='error_title'
X='file_error_title'
W='add_failed_title'
V='invalid_selected_index'
U='update_failed_title'
T='word_general'
S='index'
R='save'
Q='日本語'
P='English'
O=str
N='metadata'
M='app_title'
L='readonly'
K='Segoe UI'
J='1.0'
I='i'
H=False
G=True
F=None
D=''
import tkinter as B
from tkinter import ttk as C,filedialog as Ai,messagebox as E
import json as Ad,re
class Ap:
	def __init__(A,master):Ar='Delete Entry';Aq="檔案已成功儲存到 '{0}'。";Ap="檔案 '{0}' 已成功載入。";Ao='載入檔案時發生錯誤: {0}';An='檔案未找到。';Am='無法解析JSON檔案。請確保檔案格式正確。';Ak='詞條已刪除。';Aj='原詞條缺少索引資訊。';Ai='詞條已更新。';Ah='詞彙語言 (ISO 639-1):';Ag='詞彙表描述:';Af='詞彙表作者:';Ae='詞彙表名稱:';Ad='易混詞 (每行一個):';Ac='詞彙 - 日語 Kanji 形式:';Ab='詞彙 - 假名形式:';Aa='詞彙語言和解釋語言不能相同。';AZ='您確定要刪除此詞條嗎？';AW='請先從列表中選擇一個詞條。';f='刪除成功';e='確認刪除';d='新詞條已新增。';c='新增成功';b='更新成功';O='未知作者';L='新詞彙表';K='解釋語言 (ISO 639-1):';J='索引:';I='MemoWord 詞彙表編輯器';G='刪除詞條';E='add_new_entry_msg';D='index_must_be_int';C='input_error_title';A.master=master;A.master.geometry('1000x700');A.master.title(I);A.data=[];A.metadata=F;A.current_file_path=F;A.selected_entry_id=F;A.unsaved_changes=H;A.LANG_TO_ISO={'中文 (简体)':'zh-Hans',P:'en',Q:'ja','Français':'fr','Español':'es','Deutsch':'de','한국어':'ko','Português':'pt','Italiano':'it','Русский':'ru','العربية':'ar','हिन्दी':'hi','বাংলা':'bn','اردو':'ur','Bahasa Indonesia':'id','Türkçe':'tr','Tiếng Việt':'vi','ไทย':'th','Polski':'pl','Nederlands':'nl','Svenska':'sv','Norsk':'no','Dansk':'da','Suomi':'fi','Ελληνικά':'el','עבריة':'he','فارسی':'fa','Română':'ro','Magyar':'hu','Čeština':'cs','Slovenčina':'sk','Українська':'uk','Български':'bg','Hrvatski':'hr','Srpski':'sr','Català':'ca','Eesti':'et','Latviešu':'lv','Lietuvių':'lt','Slovenščina':'sl','Afrikaans':'af','Shqip':'sq','Amharic':'am','Azərbaycan dili':'az','Беларуская':'be','Bosanski':'bs','ქართული':'ka','Kurdî':'ku','ລາວ':'lo','Македонски':'mk','Монгол':'mn','непальский':'ne','Oʻzbek':'uz','ਪੰਜਾਬੀ':'pa','සිංහල':'si','Sunda':'su','Kiswahili':'sw','Tagalog':'tl','தமிழ்':'ta','తెలుగు':'te','Ўзбек':'uz','Zulu':'zu'};A.ISO_TO_LANG={B:A for(A,B)in A.LANG_TO_ISO.items()};A.translations={'简体中文':{M:'MemoWord 词汇表编辑器',g:'文件操作',h:'打开',R:'保存',i:'另存为',N:'元数据',j:'语言设置',k:'词汇语言:',l:'解释语言:',m:'词汇列表',n:'编辑词条',S:J,o:'词汇 - 假名形式:',p:'词汇 - 日语 Kanji 形式:',T:'词汇:',q:'解释:',r:'易混词 (每行一个):',s:'新增词条',t:'更新词条',u:'删除词条',v:'退出确认',w:'您有未保存的更改。是否要保存？',x:'缺少元数据',y:'此文件缺少元数据。是否现在填写？\n(推荐填写，否则将以空元数据保存)',z:'编辑元数据',A0:'词汇表名称:',A1:'词彙表作者:',A2:'词彙表描述:',A3:'词彙語言 (ISO 639-1):',A4:K,A5:L,A6:O,A7:'取消元数据',A8:'您尚未保存元数据。是否确定不保存并退出？\n(这将导致文件保存失败或元数据为空)',C:'输入错误',D:'索引必须是整数。',A9:'选择错误',AA:'无法找到对应的词条数据。',E:'已清空表单，请填写新词条信息。新词条索引为 {0}。',AB:b,AC:'词条已更新。',U:'更新失败',AD:'原词条缺少索引信息。',V:'选择的词条索引无效。',W:'新增失败',AE:'无法获取新词条的有效索引。',AF:'索引 {0} 已存在，请使用不同的索引或选择现有词条进行更新。',AG:c,AH:d,AI:'删除詞條',AJ:AW,AK:e,AL:AZ,AM:f,AN:'詞條已删除。',X:'文件錯誤',AO:'無法解析JSON文件。請確保文件格式正確。',AP:'文件未找到。',Y:'錯誤',AQ:'加載文件時發生錯誤: {0}',AR:'加載成功',AS:"文件 '{0}' 已成功加載。",Z:'保存文件',a:'沒有數據可供保存。',AT:'保存成功',AU:"文件已成功保存到 '{0}'。",AV:'界面語言:',AX:'語言衝突',AY:Aa},'繁體中文':{M:I,g:'檔案操作',h:'開啟',R:'儲存',i:'另存為',N:'元數據',j:'語言設定',k:'詞彙語言:',l:'解釋語言:',m:'詞彙列表',n:'編輯詞條',S:J,o:Ab,p:Ac,T:'詞彙:',q:'解釋:',r:Ad,s:'新增詞條',t:'更新詞條',u:G,v:'退出確認',w:'您有未儲存的更改。是否要儲存？',x:'缺少元數據',y:'此檔案缺少元數據。是否現在填寫？\n(推薦填寫，否則將以空元數據儲存)',z:'編輯元數據',A0:Ae,A1:Af,A2:Ag,A3:Ah,A4:K,A5:L,A6:O,A7:'取消元數據',A8:'您尚未儲存元數據。是否確定不儲存並退出？\n(這將導致檔案儲存失敗或元數據為空)',C:'輸入錯誤',D:'索引必須是整數。',A9:'選擇錯誤',AA:'無法找到對應的詞條資料。',E:'已清空表單，請填寫新詞條資訊。新詞條索引為 {0}。',AB:b,AC:Ai,U:'更新失敗',AD:Aj,V:'選擇的詞條索引無效。',W:'新增失敗',AE:'無法取得新詞條的有效索引。',AF:'索引 {0} 已存在，請使用不同的索引或選擇現有詞條進行更新。',AG:c,AH:d,AI:G,AJ:AW,AK:e,AL:AZ,AM:f,AN:Ak,X:'檔案錯誤',AO:Am,AP:An,Y:'錯誤',AQ:Ao,AR:'載入成功',AS:Ap,Z:'儲存檔案',a:'沒有資料可供儲存。',AT:'儲存成功',AU:Aq,AV:'介面語言:',AX:'語言衝突',AY:Aa},'粵語':{M:I,g:'檔案操作',h:'開啟',R:'儲存',i:'另存為',N:'元數據',j:'語言設定',k:'詞彙語言:',l:'解釋語言:',m:'詞彙列表',n:'編輯詞條',S:J,o:Ab,p:Ac,T:'詞彙:',q:'解釋:',r:Ad,s:'新增詞條',t:'更新詞條',u:G,v:'退出確認',w:'您有未儲存嘅更改。係咪要儲存？',x:'缺少元數據',y:'呢個檔案缺少元數據。而家填寫？\n(建議填寫，否則會以空元數據儲存)',z:'編輯元數據',A0:Ae,A1:Af,A2:Ag,A3:Ah,A4:K,A5:L,A6:O,A7:'取消元數據',A8:'您仲未儲存元數據。係咪確定唔儲存就離開？\n(咁會導致檔案儲存失敗或者元數據係空嘅)',C:'輸入錯誤',D:'索引必須係整數。',A9:'選擇錯誤',AA:'搵唔到對應嘅詞條資料。',E:'已清空表單，請填寫新詞條資訊。新詞條索引係 {0}。',AB:b,AC:Ai,U:'更新失敗',AD:Aj,V:'選擇嘅詞條索引無效。',W:'新增失敗',AE:'攞唔到新詞條嘅有效索引。',AF:'索引 {0} 已存在，請使用唔同嘅索引或者選擇現有詞條更新。',AG:c,AH:d,AI:G,AJ:'請先喺列表揀一個詞條。',AK:e,AL:'您確定要刪除呢個詞條嗎？',AM:f,AN:Ak,X:'檔案錯誤',AO:Am,AP:An,Y:'錯誤',AQ:Ao,AR:'載入成功',AS:Ap,Z:'儲存檔案',a:'冇資料可以儲存。',AT:'儲存成功',AU:Aq,AV:'介面語言:'},P:{M:'MemoWord Vocabulary Editor',g:'File Operations',h:'Open',R:'Save',i:'Save As',N:'Metadata',j:'Language Settings',k:'Vocabulary Language:',l:'Explanation Language:',m:'Vocabulary List',n:'Edit Entry',S:'Index:',o:'Word - Kana Form:',p:'Word - Kanji Form:',T:'Word:',q:'Explanation:',r:'Confusable Words (one per line):',s:'Add New Entry',t:'Update Entry',u:Ar,v:'Exit Confirmation',w:'You have unsaved changes. Do you want to save?',x:'Missing Metadata',y:'This file is missing metadata. Do you want to fill it in now?\n(Recommended, otherwise it will be saved with empty metadata)',z:'Edit Metadata',A0:'Vocabulary Name:',A1:'Vocabulary Author:',A2:'Vocabulary Description:',A3:'Vocabulary Language (ISO 639-1):',A4:'Explanation Language (ISO 639-1):',A5:'New Vocabulary',A6:'Unknown Author',A7:'Cancel Metadata',A8:'You have not saved metadata. Are you sure you want to exit without saving?\n(This will cause file save to fail or metadata to be empty)',C:'Input Error',D:'Index must be an integer.',A9:'Selection Error',AA:'Could not find corresponding entry data.',E:'Form cleared. Please fill in new entry information. New entry index is {0}.',AB:'Update Successful',AC:'Entry updated.',U:'Update Failed',AD:'Original entry is missing index information.',V:'Selected entry index is invalid.',W:'Add Failed',AE:'Could not get a valid index for the new entry.',AF:'Index {0} already exists. Please use a different index or select an existing entry to update.',AG:'Add Successful',AH:'New entry added.',AI:Ar,AJ:'Please select an entry from the list first.',AK:'Confirm Deletion',AL:'Are you sure you want to delete this entry?',AM:'Delete Successful',AN:'Entry deleted.',X:'File Error',AO:'Could not parse JSON file. Please ensure the file format is correct.',AP:'File not found.',Y:'Error',AQ:'An error occurred while loading the file: {0}',AR:'Load Successful',AS:"File '{0}' loaded successfully.",Z:'Save File',a:'No data to save.',AT:'Save Successful',AU:"File successfully saved to '{0}'.",AV:'UI Language:'}};A.ui_language_var=B.StringVar(value=P);A.current_ui_language=A.ui_language_var.get();A.APP_BG_COLOR='#f8f9fa';A.INPUT_FIELD_BG_COLOR='#ffffff';A._apply_styles();A._create_widgets();A._set_ui_language();A.vocab_lang_var.set(P);A.explanation_lang_var.set(Q);A._update_treeview();A._add_new_entry_mode();A.master.protocol(Al,A._on_closing)
	def _apply_styles(B):
		S='selected';R='Treeview';Q='TCombobox';P='vista';O='clam';N='#ced4da';M='#495057';J='bold';I='flat';H='pressed';G='active';F='#343a40';E='white';A=C.Style()
		if O in A.theme_names():A.theme_use(O)
		elif P in A.theme_names():A.theme_use(P)
		else:A.theme_use('default')
		B.master.configure(bg=B.APP_BG_COLOR);A.configure('TFrame',background=B.APP_BG_COLOR);A.configure('TLabelFrame',background=B.APP_BG_COLOR,foreground=F,font=(K,10,J));A.configure('TLabelFrame.Label',background=B.APP_BG_COLOR,foreground=F);A.configure(b,font=(K,10,J),background='#28a745',foreground=E,padding=8,relief=I,focusthickness=0,focuscolor=D);A.map(b,background=[(G,'#218838'),(H,'#1e7e34')],foreground=[(G,E),(H,E)]);A.configure(c,font=(K,10),background='#007bff',foreground=E,padding=8,relief=I,focusthickness=0,focuscolor=D);A.map(c,background=[(G,'#0056b3'),(H,'#004085')],foreground=[(G,E),(H,E)]);A.configure(Af,font=(K,10),background='#dc3545',foreground=E,padding=8,relief=I,focusthickness=0,focuscolor=D);A.map(Af,background=[(G,'#c82333'),(H,'#bd2130')],foreground=[(G,E),(H,E)]);A.configure('TEntry',fieldbackground=B.INPUT_FIELD_BG_COLOR,foreground=M,padding=5,relief=AW,borderwidth=1,bordercolor=N);A.configure('TLabel',background=B.APP_BG_COLOR,foreground=F,font=(K,9));A.configure(Q,fieldbackground=B.INPUT_FIELD_BG_COLOR,background=B.INPUT_FIELD_BG_COLOR,foreground=M,arrowcolor=F,padding=5,relief=AW,borderwidth=1,bordercolor=N);A.map(Q,fieldbackground=[(L,B.INPUT_FIELD_BG_COLOR)],selectbackground=[(L,'#e0e0e0')],selectforeground=[(L,'#333333')]);A.configure(R,background=B.INPUT_FIELD_BG_COLOR,foreground=F,fieldbackground=B.INPUT_FIELD_BG_COLOR,rowheight=28,relief=I,borderwidth=1,bordercolor=N);A.configure('Treeview.Heading',font=(K,10,J),background='#e9ecef',foreground=M,relief=I,padding=(5,8));A.map(R,background=[(S,'#cce5ff')],foreground=[(S,F)])
	def _translate(A,key,*B):C=A.translations.get(A.current_ui_language,{}).get(key,key);return C.format(*B)if B else C
	def _set_ui_language(A,event=F):A.current_ui_language=A.ui_language_var.get();A.master.title(A._translate(M));A.file_buttons_frame.config(text=A._translate(g));A.open_button.config(text=A._translate(h));A.save_button.config(text=A._translate(R));A.save_as_button.config(text=A._translate(i));A.metadata_button.config(text=A._translate(N));A.language_frame.config(text=A._translate(j));A.vocab_lang_label.config(text=A._translate(k));A.explanation_lang_label.config(text=A._translate(l));A.ui_lang_label.config(text=A._translate(AV));A.list_frame.config(text=A._translate(m));A.tree.heading(AZ,text=A._translate(S));A.tree.heading(Aa,text=A._translate(T));A.edit_frame.config(text=A._translate(n));A.index_label_text.set(A._translate(S));A.explanation_label.config(text=A._translate(q));A.confusable_words_label.config(text=A._translate(r));A.update_button.config(text=A._translate(t));A.delete_button.config(text=A._translate(u));A.add_new_entry_button.config(text=A._translate(s));A._on_vocabulary_language_change()
	def _create_widgets(A):J='<<ComboboxSelected>>';F='ew';H=C.Frame(A.master,padding=Ab);H.pack(fill=B.X);A.file_buttons_frame=C.LabelFrame(H,text=D,padding=d);A.file_buttons_frame.pack(side=B.LEFT,padx=10,pady=5);A.open_button=C.Button(A.file_buttons_frame,text=D,command=A._open_file_dialog,style=c);A.open_button.grid(row=0,column=0,padx=5,pady=2,sticky=F);A.save_button=C.Button(A.file_buttons_frame,text=D,command=A._save_file_dialog,style=b);A.save_button.grid(row=0,column=1,padx=5,pady=2,sticky=F);A.save_as_button=C.Button(A.file_buttons_frame,text=D,command=A._save_as_file_dialog,style=c);A.save_as_button.grid(row=1,column=0,padx=5,pady=2,sticky=F);A.metadata_button=C.Button(A.file_buttons_frame,text=D,command=A._open_metadata_dialog,style=c);A.metadata_button.grid(row=1,column=1,padx=5,pady=2,sticky=F);A.file_buttons_frame.grid_columnconfigure(0,weight=1);A.file_buttons_frame.grid_columnconfigure(1,weight=1);M=Ae(e(A.LANG_TO_ISO.keys()));A.language_frame=C.LabelFrame(H,text=D,padding=d);A.language_frame.pack(side=B.LEFT,padx=10,pady=5);A.vocab_lang_label=C.Label(A.language_frame,text=D);A.vocab_lang_label.pack(side=B.LEFT,padx=5);A.vocab_lang_var=B.StringVar(value=P);A.vocab_lang_combobox=C.Combobox(A.language_frame,textvariable=A.vocab_lang_var,values=M,state=L);A.vocab_lang_combobox.pack(side=B.LEFT,padx=5);A.vocab_lang_combobox.bind(J,A._on_vocabulary_language_change);A.explanation_lang_label=C.Label(A.language_frame,text=D);A.explanation_lang_label.pack(side=B.LEFT,padx=5);A.explanation_lang_var=B.StringVar(value=Q);A.explanation_lang_combobox=C.Combobox(A.language_frame,textvariable=A.explanation_lang_var,values=M,state=L);A.explanation_lang_combobox.pack(side=B.LEFT,padx=5);A.explanation_lang_combobox.bind(J,A._on_explanation_language_change);I=C.Frame(A.master,padding=Ab);I.pack(fill=B.BOTH,expand=G);A.list_frame=C.LabelFrame(I,text=D,padding=d);A.list_frame.pack(side=B.LEFT,fill=B.BOTH,expand=G,padx=(0,10));A.tree=C.Treeview(A.list_frame,columns=(AZ,Aa),show='headings');A.tree.heading(AZ,text=D);A.tree.heading(Aa,text=D);A.tree.column(AZ,width=50,stretch=B.NO);A.tree.column(Aa,width=250,stretch=B.YES);A.tree.pack(side=B.LEFT,fill=B.BOTH,expand=G);N=C.Scrollbar(A.list_frame,orient=Ac,command=A.tree.yview);N.pack(side=B.RIGHT,fill=B.Y);A.tree.configure(yscrollcommand=N.set);A.tree.bind('<<TreeviewSelect>>',A._on_treeview_select);A.tree.bind('<Button-1>',A._on_treeview_click);A.edit_frame=C.LabelFrame(I,text=D,padding=Ab);A.edit_frame.pack(side=B.RIGHT,fill=B.BOTH,expand=G);A.index_label_text=B.StringVar(value=D);C.Label(A.edit_frame,textvariable=A.index_label_text).grid(row=0,column=0,sticky=B.W,pady=2);A.i_var=B.StringVar();A.i_label=C.Label(A.edit_frame,textvariable=A.i_var);A.i_label.grid(row=0,column=1,sticky=(B.W,B.E),pady=2);A.w_main_label_text=B.StringVar(value=D);C.Label(A.edit_frame,textvariable=A.w_main_label_text).grid(row=1,column=0,sticky=B.W,pady=2);A.w_kana_entry=C.Entry(A.edit_frame,width=40);A.w_kana_entry.grid(row=1,column=1,sticky=(B.W,B.E),pady=2);A.w_kanji_label_text=B.StringVar(value=D);A.kanji_label=C.Label(A.edit_frame,textvariable=A.w_kanji_label_text);A.kanji_label.grid(row=2,column=0,sticky=B.W,pady=2);A.w_kanji_entry=C.Entry(A.edit_frame,width=40);A.w_kanji_entry.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);A.explanation_label=C.Label(A.edit_frame,text=D);A.explanation_label.grid(row=3,column=0,sticky=B.W,pady=2);A.d_text=B.Text(A.edit_frame,height=5,width=40,wrap=B.WORD,font=(K,9),relief=AW,borderwidth=1,background=A.INPUT_FIELD_BG_COLOR);A.d_text.grid(row=3,column=1,sticky=(B.W,B.E),pady=2);O=C.Scrollbar(A.edit_frame,orient=Ac,command=A.d_text.yview);O.grid(row=3,column=2,sticky=B.NS);A.d_text.configure(yscrollcommand=O.set);A.confusable_words_label=C.Label(A.edit_frame,text=D);A.confusable_words_label.grid(row=4,column=0,sticky=B.W,pady=2);A.o_text=B.Text(A.edit_frame,height=5,width=40,wrap=B.WORD,font=(K,9),relief=AW,borderwidth=1,background=A.INPUT_FIELD_BG_COLOR);A.o_text.grid(row=4,column=1,sticky=(B.W,B.E),pady=2);R=C.Scrollbar(A.edit_frame,orient=Ac,command=A.o_text.yview);R.grid(row=4,column=2,sticky=B.NS);A.o_text.configure(yscrollcommand=R.set);E=C.Frame(A.edit_frame,padding=d);E.grid(row=5,column=0,columnspan=3,pady=10);A.add_new_entry_button=C.Button(E,text=D,command=A._add_new_entry_mode,style=b);A.add_new_entry_button.pack(side=B.LEFT,padx=5);A.add_new_entry_button.pack_forget();A.update_button=C.Button(E,text=D,command=A._update_entry,style=b);A.update_button.pack(side=B.LEFT,padx=5);A.delete_button=C.Button(E,text=D,command=A._delete_entry,style=Af);A.delete_button.pack(side=B.LEFT,padx=5);A.edit_frame.grid_columnconfigure(1,weight=1);A.edit_frame.grid_rowconfigure(3,weight=1);A.edit_frame.grid_rowconfigure(4,weight=1);A.bottom_right_frame=C.Frame(A.master,padding=d);A.bottom_right_frame.pack(side=B.BOTTOM,anchor=B.SE,padx=10,pady=5);A.ui_lang_label=C.Label(A.bottom_right_frame,text=D);A.ui_lang_label.pack(side=B.LEFT,padx=5);A.ui_language_combobox=C.Combobox(A.bottom_right_frame,textvariable=A.ui_language_var,values=['简体中文','繁體中文','粵語',P],state=L,width=15);A.ui_language_combobox.pack(side=B.LEFT,padx=5);A.ui_language_combobox.bind(J,A._set_ui_language)
	def _update_treeview(A):
		for E in A.tree.get_children():A.tree.delete(E)
		for(F,C)in Aj(A.data):G=C.get(I,D);H=C.get('w',D);A.tree.insert(D,B.END,iid=O(F),values=(G,H))
	def _clear_entry_form(A):A.i_var.set(D);A.w_kana_entry.delete(0,B.END);A.w_kanji_entry.delete(0,B.END);A.d_text.delete(J,B.END);A.o_text.delete(J,B.END);A.add_new_entry_button.pack_forget()
	def _populate_entry_form(A,entry_data):
		C=entry_data;A.i_var.set(O(C.get(I,D)));F=C.get('w',D)
		if A.vocab_lang_var.get()==Q:
			E=re.match('^(.*?)(?:〔(.*?)〕)?$',F)
			if E:G=E.group(1);H=E.group(2)if E.group(2)else D;A.w_kana_entry.delete(0,B.END);A.w_kana_entry.insert(0,G);A.w_kanji_entry.delete(0,B.END);A.w_kanji_entry.insert(0,H)
			else:A.w_kana_entry.delete(0,B.END);A.w_kana_entry.insert(0,F);A.w_kanji_entry.delete(0,B.END)
		else:A.w_kana_entry.delete(0,B.END);A.w_kana_entry.insert(0,F);A.w_kanji_entry.delete(0,B.END);A.w_kanji_entry.grid_forget()
		A.d_text.delete(J,B.END);A.d_text.insert(J,C.get('d',D));K=C.get('o',[]);A.o_text.delete(J,B.END);A.o_text.insert(J,'\n'.join(K));A.add_new_entry_button.pack(side=B.LEFT,padx=5)
	def _get_form_data(A):
		E=A.w_kana_entry.get().strip();F=A.w_kanji_entry.get().strip();C=D
		if A.vocab_lang_var.get()==Q and F:C=f"{E}〔{F}〕"
		else:C=E
		G=A.d_text.get(J,B.END).strip();H=A.o_text.get(J,B.END).strip();I=[A.strip()for A in H.split('\n')if A.strip()];return{'w':C,'d':G,'o':I}
	def _on_treeview_select(A,event):
		B=A.tree.selection()
		if not B:return
		A.selected_entry_id=B[0];C=f(A.selected_entry_id)
		if 0<=C<len(A.data):A._populate_entry_form(A.data[C])
		else:A._clear_entry_form();E.showwarning(A._translate(A9),A._translate(AA))
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
		A.i_var.set(O(B));A.selected_entry_id=F;A.add_new_entry_button.pack_forget()
	def _update_entry(A):
		D=A._get_form_data()
		if D is F:return
		B=F
		if A.selected_entry_id is not F:
			H=f(A.selected_entry_id)
			if 0<=H<len(A.data):
				J=A.data[H].get(I)
				if J is F:E.showerror(A._translate(U),A._translate(AD));return
				L={**D,I:J};A.data[H]=L;B=J;E.showinfo(A._translate(AB),A._translate(AC))
			else:E.showerror(A._translate(U),A._translate(V));return
		else:
			try:C=f(A.i_var.get())
			except ValueError:E.showerror(A._translate(W),A._translate(AE));return
			M={A[I]for A in A.data if I in A}
			if C in M:E.showerror(A._translate(W),A._translate(AF,C));return
			N={**D,I:C};A.data.append(N);A.data.sort(key=lambda x:x.get(I,float('inf')));B=C;E.showinfo(A._translate(AG),A._translate(AH))
		A._update_treeview()
		if B is not F:
			for(K,P)in Aj(A.data):
				if P.get(I)==B:A.tree.selection_set(O(K));A.tree.focus(O(K));A.selected_entry_id=O(K);break
		A.unsaved_changes=G
	def _delete_entry(A):
		if A.selected_entry_id is F:E.showwarning(A._translate(AI),A._translate(AJ));return
		C=E.askyesno(A._translate(AK),A._translate(AL))
		if C:
			B=f(A.selected_entry_id)
			if 0<=B<len(A.data):del A.data[B];A._update_treeview();A._add_new_entry_mode();E.showinfo(A._translate(AM),A._translate(AN));A.unsaved_changes=G
			else:E.showerror(A._translate('delete_failed_title'),A._translate(V))
	def _open_file_dialog(B):
		A=Ai.askopenfilename(defaultextension='.json',filetypes=[(Am,An),(Ao,'*.*')])
		if A:B._load_json(A)
	def _load_json(A,file_path):
		C=file_path
		try:
			with open(C,'r',encoding='utf-8')as D:B=Ad.load(D)
			A.data=[];A.metadata=F
			if B and isinstance(B,e)and B[0].get(N)is G:A.metadata=B.pop(0);A.data=B
			else:A.data=B
			A.current_file_path=C;A.master.title(f"{A._translate(M)} - {C}");A._update_treeview();A._clear_entry_form();A._add_new_entry_mode();A.unsaved_changes=H;E.showinfo(A._translate(AR),A._translate(AS,C))
		except Ad.JSONDecodeError:E.showerror(A._translate(X),A._translate(AO))
		except FileNotFoundError:E.showerror(A._translate(X),A._translate(AP))
		except Ak as I:E.showerror(A._translate(Y),A._translate(AQ,I))
	def _save_file_dialog(A):
		if not A.data and not A.metadata:E.showwarning(A._translate(Z),A._translate(a));return H
		if A.current_file_path:return A._save_json(A.current_file_path)
		else:return A._save_as_file_dialog()
	def _save_as_file_dialog(A):
		if not A.data and not A.metadata:E.showwarning(A._translate(Z),A._translate(a));return H
		B=Ai.asksaveasfilename(defaultextension='.json',filetypes=[(Am,An),(Ao,'*.*')])
		if B:return A._save_json(B)
		return H
	def _save_json(A,file_path):
		B=file_path
		if A.metadata is F:
			J=E.askyesno(A._translate(x),A._translate(y))
			if J:
				if not A._open_metadata_dialog(force_save=G):return H
		try:
			C=e(A.data)
			if A.metadata:
				if A.vocab_lang_var.get()and A.explanation_lang_var.get():A.metadata[Ag]=A.LANG_TO_ISO.get(A.vocab_lang_var.get(),D);A.metadata[Ah]=A.LANG_TO_ISO.get(A.explanation_lang_var.get(),D)
				C.insert(0,A.metadata)
			C[1:].sort(key=lambda x:x.get(I,float('inf')))
			with open(B,'w',encoding='utf-8')as K:Ad.dump(C,K,ensure_ascii=H,indent=4)
			A.current_file_path=B;A.master.title(f"{A._translate(M)} - {B}");A.unsaved_changes=H;E.showinfo(A._translate(AT),A._translate(AU,B));return G
		except Ak as L:E.showerror(A._translate(Y),A._translate('file_save_error',L));return H
	def _check_language_conflict(A):
		B=A.vocab_lang_var.get();C=A.explanation_lang_var.get()
		if B and C and B==C:E.showwarning(A._translate(AX),A._translate(AY));return G
		return H
	def _on_vocabulary_language_change(A,event=F):
		if A._check_language_conflict():0
		E=A.vocab_lang_var.get()
		if E==Q:A.w_main_label_text.set(A._translate(o));A.w_kanji_label_text.set(A._translate(p));A.kanji_label.grid(row=2,column=0,sticky=B.W,pady=2);A.w_kanji_entry.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);A.w_kana_entry.config(state=B.NORMAL)
		else:A.w_main_label_text.set(A._translate(T));A.w_kanji_label_text.set(D);A.kanji_label.grid_forget();A.w_kanji_entry.grid_forget();A.w_kanji_entry.delete(0,B.END);A.w_kana_entry.config(state=B.NORMAL)
		if A.selected_entry_id is not F:
			C=f(A.selected_entry_id)
			if 0<=C<len(A.data):A._populate_entry_form(A.data[C])
	def _on_explanation_language_change(A,event=F):
		if A._check_language_conflict():0
	def _on_closing(A):
		if A.unsaved_changes:B=E.askyesnocancel(A._translate(v),A._translate(w))
		else:A.master.destroy()
	def _open_metadata_dialog(A,force_save=H):
		Y='description';X='author';W='name';F=B.Toplevel(A.master);F.title(A._translate(z));F.transient(A.master);F.grab_set();F.geometry('400x300');F.configure(bg=A.APP_BG_COLOR);I=C.Frame(F,padding=Ab);I.pack(fill=B.BOTH,expand=G);C.Label(I,text=A._translate(A0)).grid(row=0,column=0,sticky=B.W,pady=2);Q=B.StringVar();Z=C.Entry(I,textvariable=Q,width=40);Z.grid(row=0,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(A1)).grid(row=1,column=0,sticky=B.W,pady=2);S=B.StringVar();a=C.Entry(I,textvariable=S,width=40);a.grid(row=1,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(A2)).grid(row=2,column=0,sticky=B.W,pady=2);M=B.Text(I,height=5,width=40,wrap=B.WORD,font=(K,9),relief=AW,borderwidth=1,background=A.INPUT_FIELD_BG_COLOR);M.grid(row=2,column=1,sticky=(B.W,B.E),pady=2);U=C.Scrollbar(I,orient=Ac,command=M.yview);U.grid(row=2,column=2,sticky=B.NS);M.configure(yscrollcommand=U.set);C.Label(I,text=A._translate(A3)).grid(row=3,column=0,sticky=B.W,pady=2);O=B.StringVar();f=C.Combobox(I,textvariable=O,values=Ae(e(A.ISO_TO_LANG.keys())),state=L,width=37);f.grid(row=3,column=1,sticky=(B.W,B.E),pady=2);C.Label(I,text=A._translate(A4)).grid(row=4,column=0,sticky=B.W,pady=2);P=B.StringVar();g=C.Combobox(I,textvariable=P,values=Ae(e(A.ISO_TO_LANG.keys())),state=L,width=37);g.grid(row=4,column=1,sticky=(B.W,B.E),pady=2)
		if A.metadata:Q.set(A.metadata.get(W,D));S.set(A.metadata.get(X,D));M.insert(J,A.metadata.get(Y,D));O.set(A.metadata.get(Ag,D));P.set(A.metadata.get(Ah,D))
		else:Q.set(A._translate(A5));S.set(A._translate(A6));O.set(A.LANG_TO_ISO.get(A.vocab_lang_var.get(),D));P.set(A.LANG_TO_ISO.get(A.explanation_lang_var.get(),D))
		def h():
			if O.get()==P.get():E.showwarning(A._translate(AX),A._translate(AY));return
			A.metadata={N:G,W:Q.get().strip(),X:S.get().strip(),Y:M.get(J,B.END).strip(),Ag:O.get().strip(),Ah:P.get().strip()};A.unsaved_changes=G;F.destroy()
		def V():
			if force_save:
				B=E.askyesno(A._translate(A7),A._translate(A8))
				if B:F.destroy();F.result=H
			else:F.destroy();F.result=H
		T=C.Frame(I,padding=d);T.grid(row=5,column=0,columnspan=3,pady=10);C.Button(T,text=A._translate(R),command=h,style=b).pack(side=B.LEFT,padx=5);C.Button(T,text=A._translate('cancel_metadata'),command=V,style=c).pack(side=B.LEFT,padx=5);F.protocol(Al,V);A.master.wait_window(F);return getattr(F,'result',G)
if __name__=='__main__':A=B.Tk();Aq=Ap(A);A.mainloop()