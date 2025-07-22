Ac='settings'
Ab='session_start_count'
Aa='direct'
AZ='horizontal'
AY='QuizFeedback.TLabel'
AX='QuizQuestion.TLabel'
AW='LearningRomaji.TLabel'
AV='LearningBracketed.TLabel'
AU='LearningSimilar.TLabel'
AT='LearningDefinition.TLabel'
AS='LearningWord.TLabel'
AR='volume'
AQ='WM_DELETE_WINDOW'
AP=enumerate
AO=ImportError
AN='跟随系统设置'
AM='不显示'
AL='text'
AK='Obvious'
AJ='None'
AI='〔.*?〕'
AH='vocabulary_data'
AG='utf-8'
AF='Incorrect.QuizOption.TButton'
AE='Correct.QuizOption.TButton'
AD=ValueError
AC='无解释'
AB='开始学习'
AA='Off'
A9='On'
A8='black'
A7=print
A5='bold'
A4='voice'
A3='Arial'
A2='Helvetica'
A1=range
x='N/A'
w='#2b2b2b'
v='#f0f0f0'
u='e'
t=1.
s='15'
r='QuizOption.TButton'
q='System'
p='fallback_font_family'
o='错误'
n='last_study_time'
m='Subtle'
l='enable_tts'
k='show_romaji_for_kana'
j='romaji_font_size'
i='bracketed_font_size'
h='main_word_font_size'
g=list
f=Exception
d='center'
c='tts_rate'
b='tts_volume'
a='romaji_font_family'
Z='bracketed_font_family'
Y='main_word_font_family'
X='study_count'
W='readonly'
V='i'
U='reveal_hint_style'
T='d'
S='o'
R='dark_mode'
Q='show_session_summary'
P='global_font_family'
O='ew'
N='write'
M='tts_voice_id'
L=False
K='selected_vocabulary_language'
J=True
I=len
H=''
G=None
E='FollowGlobal'
D='w'
import tkinter as C
from tkinter import ttk as B,filedialog as Ad,messagebox as F,font
import json as y
from datetime import datetime as z,timedelta as Ae
import os,random as e,re,copy,threading as Af
try:import darkdetect as A0
except AO:A0=G
try:import pyttsx3 as A6
except AO:A6=G
class Ag:
	def __init__(A,master):z='sso';y='sse';x='ssu';w='sshi';v='ssa';s='kko';r='kke';o='kku';n='kki';g='kka';f='mmi';e='ru';d='ri';X='zu';W='ji';T='yo';O='yu';N='ya';I='ka';H='u';F='a';C=master;B='wa';A.master=C;C.title('MemoWord - 记单词');C.geometry('800x600');C.minsize(600,400);A.vocabulary_data={};A.progress_file='memoword_progress.json';A.session_start_count=0;A.settings={P:A2,p:A3,Y:E,h:36,Z:E,i:20,a:E,j:14,U:m,Q:J,k:L,R:q,l:L,M:G,b:t,c:175,K:G};A.direct_learning_session=[];A.direct_word_index=0;A.quiz_session_words=[];A.quiz_words_to_ask=[];A.incorrectly_answered_words=[];A.current_quiz_word=G;A.current_quiz_correct_answer=G;A.quiz_items_completed=0;A.quiz_total_items_to_complete=0;A.recently_learned_for_quiz=[];A.KANA_TO_ROMAJI_MAP={'っか':g,'っき':n,'っく':o,'っけ':r,'っこ':s,'っさ':v,'っし':w,'っす':x,'っせ':y,'っそ':z,'った':'tta','っち':'cchi','っつ':'ttsu','って':'tte','っと':'tto','っぱ':'ppa','っぴ':'ppi','っぷ':'ppu','っぺ':'ppe','っぽ':'ppo','っは':'hha','っひ':'hhi','っふ':'ffu','っへ':'hhe','っほ':'hho','っま':'mma','っみ':f,'っむ':'mmu','っめ':'mme','っも':'mmo','っや':'yya','っゆ':'yyu','っよ':'yyo','っら':'rra','っり':'rri','っる':'rru','っれ':'rre','っろ':'rro','っわ':'wwa','ッか':g,'ッキ':n,'ック':o,'ッケ':r,'ッコ':s,'ッサ':v,'ッシ':w,'ッス':x,'ッセ':y,'ッソ':z,'ッタ':'tta','ッチ':'cchi','ッツ':'ttsu','ッテ':'tte','ット':'tto','ッパ':'ppa','ッピ':'ppi','ップ':'ppu','ッペ':'ppe','ッポ':'ppo','ッハ':'hha','ッヒ':'hhi','ッフ':'ffu','ッヘ':'hhe','ッホ':'hho','ッマ':'mma','ッミ':f,'ッム':'mmu','ッメ':'mme','ッモ':'mmo','ッヤ':'yya','ッユ':'yyu','ッヨ':'yyo','ッラ':'rra','ッリ':'rri','ッル':'rru','ッレ':'rre','ッロ':'rro','ッワ':'wwa','きゃ':'kya','きゅ':'kyu','きょ':'kyo','しゃ':'sha','しゅ':'shu','しょ':'sho','ちゃ':'cha','ちゅ':'chu','ちょ':'cho','にゃ':'nya','にゅ':'nyu','にょ':'nyo','ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','みゃ':'mya','みゅ':'myu','みょ':'myo','りゃ':'rya','りゅ':'ryu','りょ':'ryo','ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo','じゃ':'ja','じゅ':'ju','じょ':'jo','びゃ':'bya','びゅ':'byu','びょ':'byo','ぴゃ':'pya','ぴゅ':'pyu','ぴょ':'pyo','キャ':'kya','キュ':'kyu','キョ':'kyo','シャ':'sha','シュ':'shu','ショ':'sho','チャ':'cha','チュ':'chu','チョ':'cho','ニャ':'nya','ニュ':'nyu','ニョ':'nyo','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','ミャ':'mya','ミュ':'myu','ミョ':'myo','リャ':'rya','リュ':'ryu','リョ':'ryo','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ジャ':'ja','ジュ':'ju','ジョ':'jo','ビャ':'bya','ビュ':'byu','ビョ':'byo','ピャ':'pya','ピュ':'pyu','ピョ':'pyo','ああ':'aa','いい':'ii','うう':'uu','ええ':'ee','おお':'oo','おう':'oo','ー':'-','は':B,'へ':u,D:S,'あ':F,'い':V,'う':H,'え':u,'お':S,'か':I,'き':'ki','く':'ku','け':'ke','こ':'ko','さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to','な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':N,'ゆ':O,'よ':T,'ら':'ra',d:d,e:e,'れ':'re','ろ':'ro','わ':B,'ゐ':'wi','ゑ':'we','を':'wo','ん':'n','が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ざ':'za','じ':W,'ず':X,'ぜ':'ze','ぞ':'zo','だ':'da','ぢ':W,'づ':X,'で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ア':F,'イ':V,'ウ':H,'エ':u,'オ':S,'カ':I,'キ':'ki','ク':'ku','ケ':'ke','コ':'ko','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','マ':'ma','ミ':f,'ム':'mu','メ':'me','モ':'mo','ヤ':N,'ユ':O,'ヨ':T,'拉':'ra','リ':d,'ル':e,'レ':'re','ロ':'ro','ワ':B,'ヰ':'wi','ヱ':'we','ヲ':'wo','ン':'n','ガ':'ga','ギ':'gi','グ':'gu','ゲ':'ge','ご':'go','ザ':'za','ジ':W,'ズ':X,'ゼ':'ze','ゾ':'zo','ダ':'da','ヂ':W,'ヅ':X,'デ':'de','多':'do','バ':'ba','ビ':'bi','ブ':'bu','ベ':'be','ボ':'bo','パ':'pa','ピ':'pi','プ':'pu','ぺ':'pe','ポ':'po','ぁ':F,'ぃ':V,'ぅ':H,'ぇ':u,'ぉ':S,'ァ':F,'ィ':V,'ゥ':H,'ェ':u,'ォ':S,'ゃ':N,'ゅ':O,'ょ':T,'ャ':N,'ュ':O,'ョ':T,'ゎ':B,'ヮ':B,'ヶ':I,'ヵ':I};A.tts_engine=G;A.tts_voices=[];A.tts_thread=G;A.setup_tts();A.setup_styles();A.create_widgets();A.load_initial_data();A.master.protocol(AQ,A.on_app_close)
	def setup_tts(A):
		if A6 and not A.tts_engine:
			try:
				A.tts_engine=A6.init();A.tts_voices=A.tts_engine.getProperty('voices')
				if A.settings[M]and any(B.id==A.settings[M]for B in A.tts_voices):A.tts_engine.setProperty(A4,A.settings[M])
				else:
					C=L
					for B in A.tts_voices:
						if'zh'in B.languages or'ZH'in B.id:A.settings[M]=B.id;A.tts_engine.setProperty(A4,B.id);C=J;break
					if not C:
						for B in A.tts_voices:
							if'en'in B.languages or'EN'in B.id:A.settings[M]=B.id;A.tts_engine.setProperty(A4,B.id);C=J;break
					if not C and A.tts_voices:A.settings[M]=A.tts_voices[0].id;A.tts_engine.setProperty(A4,A.tts_voices[0].id)
				A.tts_engine.setProperty(AR,A.settings[b]);A.tts_engine.setProperty('rate',A.settings[c])
				if not A.tts_thread or not A.tts_thread.is_alive():A.tts_thread=Af.Thread(target=A._tts_run_loop,daemon=J);A.tts_thread.start()
			except f as D:F.showwarning('TTS 初始化失败',f"无法初始化文字转语音功能：{D}\n请确保已安装必要的语音包。",parent=A.master);A.tts_engine=G
		elif not A6:F.showwarning('TTS 库未安装',"pyttsx3 库未安装。文字转语音功能将不可用。\n请运行 'pip install pyttsx3' 进行安装。",parent=A.master)
	def _tts_run_loop(A):
		if A.tts_engine:
			try:A.tts_engine.runAndWait()
			except f as B:A7(f"TTS引擎运行错误: {B}")
	def speak_word(A,text):
		if A.settings[l]and A.tts_engine:
			try:A.tts_engine.stop();A.tts_engine.say(text)
			except f as B:A7(f"TTS say error: {B}")
	def setup_styles(H):
		Aa='TNotebook.Tab';AZ='!readonly';AR='TCombobox';AQ='Treeview';AP='TButton';AO='#5a5a5a';AN='#87ceeb';AM='#555555';AL='#444444';AK='#a8d8ff';AJ='#000000';AI='#0056b3';AH='bg_checkbutton';AG='fg_hint_obvious';AD='fg_hint_subtle';A6='selected';A4='#3c3c3c';A3='fg_notebook_selected_tab';A2='bg_notebook_selected_tab';A1='fg_notebook_tab';z='bg_notebook_tab';y='bg_spinbox_field';x='fg_combobox_arrow';u='bg_selected_treeview';t='fg_romaji';s='fg_incorrect_button';q='fg_correct_button';p='fg_quiz_question';o='fg_learning_word';n='fg_treeview_heading';m='bg_treeview_heading';l='fg_treeview';k='bg_treeview';d='fg_combobox_text';c='fg_similar_words';b='#ffffff';X='bg_combobox_selected';V='bg_combobox_field';U='fg_active_button';T='bg_active_button';S='bg_incorrect_button';Q='bg_correct_button';O='fg_label';N='bg_frame';M='#333333';L='fg_button';K='!disabled';J='active';I='bg_button';G='#e0e0e0';F='bg_label';C=B.Style();C.theme_use('clam');A7={N:v,F:v,O:M,I:'#dddddd',L:M,k:b,l:M,m:G,n:M,o:AI,p:AI,Q:'lightgreen',q:A8,S:'salmon',s:A8,AD:'gray',AG:'blue',c:'#666666',t:'#888888',AH:v,T:G,U:AJ,u:AK,V:b,X:AK,d:M,x:M,y:b,z:G,A1:M,A2:v,A3:AJ};AB={N:w,F:w,O:G,I:AL,L:G,k:A4,l:G,m:AM,n:G,o:AN,p:AN,Q:'#4CAF50',q:'white',S:'#FF6347',s:'white',AD:'#aaaaaa',AG:'#add8e6',c:'#bbbbbb',t:'#cccccc',AH:w,T:AM,U:b,u:AO,V:A4,X:AO,d:G,x:G,y:A4,z:AL,A1:G,A2:w,A3:b};AC=H.settings[R]
		if AC==A9:A=AB
		elif AC==AA:A=A7
		elif A0 and A0.isDark():A=AB
		else:A=A7
		D=H.settings[P];e=H.settings[Y]
		if e==E:e=D
		f=H.settings[Z]
		if f==E:f=D
		g=H.settings[a]
		if g==E:g=D
		C.configure('TFrame',background=A[N]);C.configure('TLabel',background=A[F],foreground=A[O],font=(D,10));C.configure(AP,font=(D,10),padding=6,background=A[I],foreground=A[L]);C.map(AP,background=[(J,A[T]),(K,A[I])],foreground=[(J,A[U]),(K,A[L])]);C.configure('Treeview.Heading',font=(D,10,A5),background=A[m],foreground=A[n]);C.configure(AQ,font=(D,10),rowheight=25,background=A[k],foreground=A[l]);C.map(AQ,background=[(A6,A[u])]);C.configure(AS,font=(e,H.settings[h],A5),foreground=A[o],background=A[F]);C.configure(AT,font=(D,18),foreground=A[O],background=A[F]);C.configure(AU,font=(D,12),foreground=A[c],background=A[F]);C.configure(AV,font=(f,H.settings[i]),foreground=A[c],background=A[F]);C.configure(AW,font=(g,H.settings[j]),foreground=A[t],background=A[F]);C.configure(AX,font=(D,20,A5),foreground=A[p],background=A[F],wraplength=700);C.configure(r,font=(D,14),padding=10,background=A[I],foreground=A[L]);C.map(r,background=[(J,A[T]),(K,A[I])],foreground=[(J,A[U]),(K,A[L])]);C.configure(AY,font=(D,14,A5),background=A[F]);C.configure(AE,background=A[Q],foreground=A[q]);C.map(AE,background=[(J,A[Q]),(K,A[Q])]);C.configure(AF,background=A[S],foreground=A[s]);C.map(AF,background=[(J,A[S]),(K,A[S])]);C.configure('TCheckbutton',background=A[F],foreground=A[O],font=(D,10));C.configure(AR,font=(D,10),fieldbackground=A[V],selectbackground=A[X],background=A[I],foreground=A[d],arrowcolor=A[x]);C.map(AR,fieldbackground=[(W,A[V]),(AZ,A[V])],selectbackground=[(W,A[X]),(AZ,A[X])],background=[(J,A[T]),(K,A[I])],foreground=[(J,A[U]),(K,A[L])]);C.configure('TSpinbox',font=(D,10),fieldbackground=A[y],foreground=A[d]);C.configure('TNotebook',background=A[N]);C.configure(Aa,background=A[z],foreground=A[A1]);C.map(Aa,background=[(A6,A[A2])],foreground=[(A6,A[A3])]);C.configure('TNotebook.Client',background=A[N]);H.master.config(bg=A[N])
	def create_widgets(A):A.main_frame=B.Frame(A.master,padding=s);A.main_frame.pack(fill=C.BOTH,expand=J);A.learning_frame=B.Frame(A.master,padding=s);A.progress_bar=B.Progressbar(A.learning_frame,orient=AZ,mode='determinate');A.progress_bar.pack(fill=C.X,pady=5);A.create_main_page_widgets();A.create_direct_learning_widgets();A.create_quiz_widgets()
	def create_main_page_widgets(A):H='definition';G='word';B.Label(A.main_frame,text='MemoWord 词汇表',font=(A.settings[P],18,A5)).pack(pady=15);E=B.Frame(A.main_frame);E.pack(pady=5,fill=C.X);E.grid_columnconfigure(0,weight=1);E.grid_columnconfigure(1,weight=2);E.grid_columnconfigure(2,weight=1);B.Label(E,text='选择词汇语言:').grid(row=0,column=0,padx=5,pady=5,sticky=D);A.selected_lang_var=C.StringVar();A.selected_lang_var.trace_add(N,A.on_language_selection_change);A.lang_combobox=B.Combobox(E,textvariable=A.selected_lang_var,state=W);A.lang_combobox.grid(row=0,column=1,padx=5,pady=5,sticky=O);A.total_study_label=B.Label(E,text='进入学习界面次数: 0',font=(A.settings[P],12));A.total_study_label.grid(row=0,column=2,padx=5,pady=5,sticky=u);A.vocab_tree=B.Treeview(A.main_frame,columns=(G,H,X,n),show='headings');A.vocab_tree.heading(G,text='词汇');A.vocab_tree.heading(H,text='解释');A.vocab_tree.heading(X,text='学习次数');A.vocab_tree.heading(n,text='上次学习时间');A.vocab_tree.column(G,width=150,minwidth=100,anchor=d);A.vocab_tree.column(H,width=300,minwidth=200,anchor=D);A.vocab_tree.column(X,width=100,minwidth=80,anchor=d);A.vocab_tree.column(n,width=150,minwidth=120,anchor=d);A.vocab_tree.pack(fill=C.BOTH,expand=J,pady=10);I=B.Scrollbar(A.vocab_tree,orient='vertical',command=A.vocab_tree.yview);I.pack(side='right',fill='y');A.vocab_tree.configure(yscrollcommand=I.set);F=B.Frame(A.main_frame);F.pack(pady=15);A.import_button=B.Button(F,text='导入词汇表',command=A.load_vocabulary);A.import_button.pack(side=C.LEFT,padx=10);A.start_learning_button=B.Button(F,text=AB,command=A.start_learning);A.start_learning_button.pack(side=C.LEFT,padx=10);A.settings_button=B.Button(F,text='设置',command=A.open_settings);A.settings_button.pack(side=C.LEFT,padx=10)
	def create_direct_learning_widgets(A):A.direct_learning_sub_frame=B.Frame(A.learning_frame,padding=s);A.learning_romaji_label=B.Label(A.direct_learning_sub_frame,text=H,style=AW,wraplength=700,anchor=d);A.learning_romaji_label.pack(pady=(20,0),fill=C.X);A.learning_word_label=B.Label(A.direct_learning_sub_frame,text=H,style=AS,wraplength=700,anchor=d);A.learning_word_label.pack(pady=(5,0),fill=C.X);A.learning_bracketed_label=B.Label(A.direct_learning_sub_frame,text=H,style=AV,wraplength=700,anchor=d);A.learning_bracketed_label.pack(pady=(5,20),fill=C.X);A.learning_definition_label=B.Label(A.direct_learning_sub_frame,text=H,style=AT,wraplength=700,anchor=d);A.learning_definition_label.pack(pady=20,fill=C.X);A.learning_similar_label=B.Label(A.direct_learning_sub_frame,text=H,style=AU,wraplength=700,anchor=d);A.learning_similar_label.pack(pady=10,fill=C.X);D=B.Frame(A.direct_learning_sub_frame);D.pack(pady=30);A.reveal_button=B.Button(D,text='显示解释',command=A.reveal_definition);A.reveal_button.pack(side=C.LEFT,padx=15);A.next_word_button=B.Button(D,text='下一个',command=A.next_direct_word,state=C.DISABLED);A.next_word_button.pack(side=C.LEFT,padx=15);A.back_to_main_button_direct=B.Button(A.direct_learning_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_direct.pack(pady=20)
	def create_quiz_widgets(A):
		A.quiz_sub_frame=B.Frame(A.learning_frame,padding=s);A.quiz_question_label=B.Label(A.quiz_sub_frame,text=H,style=AX,anchor=d);A.quiz_question_label.pack(pady=40,fill=C.X);A.quiz_options_frame=B.Frame(A.quiz_sub_frame);A.quiz_options_frame.pack(pady=20,fill=C.X,expand=J);A.quiz_options_frame.grid_columnconfigure(0,weight=1);A.quiz_options_frame.grid_columnconfigure(1,weight=1);A.quiz_option_buttons=[]
		for D in A1(4):E=B.Button(A.quiz_options_frame,text=f"Option {D+1}",style=r);E.grid(row=D//2,column=D%2,padx=10,pady=10,sticky=O);A.quiz_option_buttons.append(E);E.grid_forget()
		A.quiz_feedback_label=B.Label(A.quiz_sub_frame,text=H,style=AY);A.quiz_feedback_label.pack(pady=15);A.quiz_next_button=B.Button(A.quiz_sub_frame,text='下一个问题',command=A.next_quiz_question,state=C.DISABLED);A.quiz_next_button.pack(pady=10);A.back_to_main_button_quiz=B.Button(A.quiz_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_quiz.pack(pady=20)
	def show_main_page(A):A.learning_frame.pack_forget();A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack_forget();A.main_frame.pack(fill=C.BOTH,expand=J);A.update_main_page_display()
	def show_learning_page(A,mode):
		A.main_frame.pack_forget();A.learning_frame.pack(fill=C.BOTH,expand=J);A.progress_bar.config(value=0)
		if mode==Aa:A.quiz_sub_frame.pack_forget();A.direct_learning_sub_frame.pack(fill=C.BOTH,expand=J)
		elif mode=='quiz':A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack(fill=C.BOTH,expand=J)
	def load_initial_data(A):
		A.load_progress();A.update_language_combobox()
		if A.settings[K]and A.settings[K]in A.vocabulary_data:A.selected_lang_var.set(A.settings[K])
		elif A.vocabulary_data:B=g(A.vocabulary_data.keys())[0];A.selected_lang_var.set(B);A.settings[K]=B
		else:A.selected_lang_var.set(H)
		A.update_main_page_display()
	def load_vocabulary(A):
		c='lang';b='descriptionLanguage';a='vocabularyLanguage';Z='description';Y='author';W='name';P=Ad.askopenfilename(filetypes=[('JSON files','*.json')])
		if not P:return
		try:
			with open(P,'r',encoding=AG)as d:e=y.load(d)
			E=G;Q=[]
			for m in e:0
			h=[W,Y,Z,a,b]
			if not E or not all(A in E for A in h):F.showerror(o,'词汇表文件损坏：缺少或不完整的元数据。',parent=A.master);return
			B=E[a];i=E[b];j=f"词汇表名称: {E.get(W,x)}\n作者: {E.get(Y,x)}\n描述: {E.get(Z,x).replace("\\n","\n")}\n词汇语言: {B}\n解释语言: {i}";k=F.askyesno('确认导入词汇表',f"检测到以下词汇表信息:\n\n{j}\n\n是否导入此词汇表？",parent=A.master)
			if not k:return
			if B not in A.vocabulary_data:A.vocabulary_data[B]=[]
			M={A[D]:A for A in A.vocabulary_data[B]};N=[]
			for J in Q:
				L=J.get(D)
				if not L:continue
				if L in M:C=M[L];C[T]=J.get(T,C.get(T,H));C[S]=J.get(S,C.get(S,[]));C[V]=J.get(V,C.get(V,0));C[c]=B;N.append(C)
				else:N.append({V:J.get(V,0),D:L,T:J.get(T,H),S:J.get(S,[]),X:0,n:G,c:B})
			O={A[D]:A for A in N}
			for(R,l)in M.items():
				if R not in O:O[R]=l
			A.vocabulary_data[B]=g(O.values());A.vocabulary_data[B].sort(key=lambda x:x.get(V,0));A.save_progress();A.update_language_combobox();A.selected_lang_var.set(B);A.settings[K]=B;A.update_main_page_display();F.showinfo('导入成功',f"成功导入 {I(Q)} 个词汇到 '{B}' 语言。",parent=A.master)
		except y.JSONDecodeError:F.showerror(o,'无效的JSON文件格式。请确保文件内容符合JSON规范。',parent=A.master)
		except f as U:F.showerror(o,f"导入词汇时发生错误: {U}",parent=A.master);A7(f"Error during import: {U}")
		finally:A.master.focus_set()
	def update_language_combobox(A):
		B=sorted(g(A.vocabulary_data.keys()));A.lang_combobox['values']=B
		if not A.selected_lang_var.get()and B:A.selected_lang_var.set(B[0]);A.settings[K]=B[0]
		elif A.selected_lang_var.get()not in B:
			if B:A.selected_lang_var.set(B[0]);A.settings[K]=B[0]
			else:A.selected_lang_var.set(H);A.settings[K]=G
		A.save_progress()
	def on_language_selection_change(A,*C):
		B=A.selected_lang_var.get()
		if B:A.settings[K]=B;A.save_progress();A.update_main_page_display()
		else:A.settings[K]=G;A.save_progress();A.update_main_page_display()
	def load_progress(A):
		C='default'
		if os.path.exists(A.progress_file):
			try:
				with open(A.progress_file,'r',encoding=AG)as D:
					B=y.load(D)
					if isinstance(B,dict)and AH in B:A.vocabulary_data=B.get(AH,{});A.session_start_count=B.get(Ab,0);A.settings.update(B.get(Ac,{}))
					else:A.vocabulary_data={C:B};A.session_start_count=0;A.settings={P:A2,p:A3,Y:E,h:36,Z:E,i:20,a:E,j:14,U:m,Q:J,k:L,R:q,l:L,M:G,b:t,c:175,K:C if A.vocabulary_data.get(C)else G};F.showinfo('提示',"已将旧版词汇数据导入为 'default' 语言。",parent=A.master)
			except y.JSONDecodeError:F.showerror(o,'学习进度文件损坏或格式不正确，将重新创建。',parent=A.master);A.vocabulary_data={};A.session_start_count=0;A.settings={P:A2,p:A3,Y:E,h:36,Z:E,i:20,a:E,j:14,U:m,Q:J,k:L,R:q,l:L,M:G,b:t,c:175,K:G}
			except f as H:F.showerror(o,f"加载学习进度时发生错误: {H}",parent=A.master);A.vocabulary_data={};A.session_start_count=0;A.settings={P:A2,p:A3,Y:E,h:36,Z:E,i:20,a:E,j:14,U:m,Q:J,k:L,R:q,l:L,M:G,b:t,c:175,K:G}
		else:A.vocabulary_data={};A.session_start_count=0;A.settings={P:A2,p:A3,Y:E,h:36,Z:E,i:20,a:E,j:14,U:m,Q:J,k:L,R:q,l:L,M:G,b:t,c:175,K:G}
	def save_progress(A):
		try:
			B={AH:A.vocabulary_data,Ab:A.session_start_count,Ac:A.settings}
			with open(A.progress_file,D,encoding=AG)as C:y.dump(B,C,ensure_ascii=L,indent=4)
		except f as E:F.showerror(o,f"保存学习进度时发生错误: {E}",parent=A.master)
	def update_main_page_display(A):
		for G in A.vocab_tree.get_children():A.vocab_tree.delete(G)
		I=A.selected_lang_var.get();J=A.vocabulary_data.get(I,[])
		for B in J:
			K=B.get(D,x);L=B.get(T,x);M=B.get(X,0);F=B.get(n);E='未学习'
			if F:
				try:N=z.fromisoformat(F);E=N.strftime('%Y-%m-%d %H:%M')
				except AD:E='日期格式错误'
			A.vocab_tree.insert(H,C.END,values=(K,L,M,E))
		A.total_study_label.config(text=f"进入学习界面次数: {A.session_start_count}")
	def start_learning(A):
		G=A.selected_lang_var.get()
		if not G or not A.vocabulary_data.get(G):F.showwarning('提示','请先选择一个包含词汇的语言，或导入词汇表！',parent=A.master);return
		K=A.vocabulary_data[G];A.session_start_count+=1;A.save_progress();D=[];C=[];E=[];L=z.now();M=L-Ae(days=3)
		for B in K:
			H=B.get(X,0);J=B.get(n)
			if H==0:D.append(B)
			elif J:
				try:
					N=z.fromisoformat(J)
					if H<15 and N<M:C.append(B)
					else:E.append(B)
				except AD:C.append(B)
			else:C.append(B)
		D.sort(key=lambda x:x.get(V,0))
		if C:
			if A.settings[Q]:F.showinfo(AB,f"有 {I(C)} 个单词需要优先复习！",parent=A.master)
			A.start_quiz_session(C)
		elif A.recently_learned_for_quiz:
			if A.settings[Q]:F.showinfo('开始复习',f"开始复习刚刚学习的 {I(A.recently_learned_for_quiz)} 个单词！",parent=A.master)
			O=g(A.recently_learned_for_quiz);A.recently_learned_for_quiz.clear();A.start_quiz_session(O)
		elif D:
			A.direct_learning_session=D[:5]
			if A.settings[Q]:F.showinfo(AB,f"开始学习 {I(A.direct_learning_session)} 个新单词！",parent=A.master)
			A.start_direct_learning_session()
		else:
			if not E:F.showinfo('恭喜','所有单词都已学习或复习完毕！',parent=A.master);return
			e.shuffle(E);A.quiz_session_words=E[:10]
			if A.settings[Q]:F.showinfo(AB,f"开始复习 {I(A.quiz_session_words)} 个旧单词！",parent=A.master)
			A.start_quiz_session(A.quiz_session_words)
		A.master.focus_set()
	def start_direct_learning_session(A):
		A.direct_word_index=0
		if A.direct_learning_session:A.show_learning_page(Aa);A.progress_bar.config(maximum=I(A.direct_learning_session),value=0);A.display_current_direct_word()
		else:A.show_main_page()
	def _kana_to_romaji(E,kana_text):
		B=kana_text;C=[];A=0
		while A<I(B):
			M=L
			for K in A1(3,0,-1):
				if A+K<=I(B):
					D=B[A:A+K]
					if D in E.KANA_TO_ROMAJI_MAP:
						if D=='ー'and C:
							N=re.search('[aeiou]$',C[-1])
							if N:C[-1]+=N.group(0)
							else:C.append('-')
						elif D in['ん','ン']and A+1<I(B)and re.match('[あいうえおやゆよアイウエオヤユヨ]',B[A+1]):C.append("n'")
						elif D in['っ','ッ']and A+1<I(B):
							F=G
							for O in A1(3,0,-1):
								if A+1+O<=I(B):
									P=B[A+1:A+1+O]
									if P in E.KANA_TO_ROMAJI_MAP:F=E.KANA_TO_ROMAJI_MAP[P];break
							if F and F[0].isalpha():C.append(F[0])
						else:C.append(E.KANA_TO_ROMAJI_MAP[D])
						A+=K;M=J;break
			if not M:C.append(B[A]);A+=1
		return H.join(C)
	def display_current_direct_word(A):
		N="点击 '显示解释' 查看"
		if A.direct_word_index<I(A.direct_learning_session):
			G=A.direct_learning_session[A.direct_word_index];B=G.get(D,H);A.progress_bar.config(value=A.direct_word_index+1)
			if A.settings[k]:O=re.sub(AI,H,B);P=H.join(A for A in O if'\u3040'<=A<='ゟ'or'゠'<=A<='ヿ'or A=='ー');R=A._kana_to_romaji(P);A.learning_romaji_label.config(text=R)
			else:A.learning_romaji_label.config(text=H)
			J=re.search(AI,B)
			if J:K=J.group(0);L=B.replace(K,H).strip();A.learning_word_label.config(text=L);A.learning_bracketed_label.config(text=K)
			else:A.learning_word_label.config(text=B);A.learning_bracketed_label.config(text=H)
			E=A.settings[U]
			if E==AJ:A.learning_definition_label.config(text=H,foreground=A8)
			elif E==m:A.learning_definition_label.config(text=N,foreground='gray')
			elif E==AK:A.learning_definition_label.config(text=N,foreground='blue')
			M=', '.join(G.get(S,[]));A.learning_similar_label.config(text=f"形近/音近词: {M}"if M else'无形近/音近词');A.reveal_button.config(state=C.NORMAL);A.next_word_button.config(state=C.DISABLED);A.speak_word(L)
		elif A.direct_learning_session:
			A.recently_learned_for_quiz=g(A.direct_learning_session)
			if A.settings[Q]:F.showinfo('学习完成',f"本次新词学习已完成！接下来将复习刚刚学习的 {I(A.recently_learned_for_quiz)} 个单词。",parent=A.master)
			A.start_quiz_session(A.recently_learned_for_quiz)
		else:F.showinfo('学习结束','本次学习已完成！',parent=A.master);A.show_main_page()
	def reveal_definition(A):
		if A.direct_word_index<I(A.direct_learning_session):
			E=A.direct_learning_session[A.direct_word_index];A.learning_definition_label.config(text=E.get(T,AC),foreground=A8);A.reveal_button.config(state=C.DISABLED);A.next_word_button.config(state=C.NORMAL);H=E.get(D);B=A.settings[K]
			if B and B in A.vocabulary_data:
				for(F,G)in AP(A.vocabulary_data[B]):
					if G.get(D)==H:A.vocabulary_data[B][F][X]=G.get(X,0)+1;A.vocabulary_data[B][F][n]=z.now().isoformat();break
			A.save_progress()
	def next_direct_word(A):A.direct_word_index+=1;A.display_current_direct_word()
	def start_quiz_session(A,words_to_quiz_initial=G):
		C=words_to_quiz_initial;A.incorrectly_answered_words=[];A.quiz_items_completed=0;A.quiz_words_to_ask=[];B=[]
		if C is not G:B=g(C)
		else:B=g(A.quiz_session_words)
		for D in B:
			for E in A1(3):A.quiz_words_to_ask.append(D)
		e.shuffle(A.quiz_words_to_ask);A.quiz_total_items_to_complete=I(A.quiz_words_to_ask)
		if A.quiz_words_to_ask:A.show_learning_page('quiz');A.progress_bar.config(maximum=A.quiz_total_items_to_complete,value=A.quiz_items_completed);A.display_quiz_question()
		else:F.showinfo('测验结束','本次测验已完成！',parent=A.master);A.show_main_page()
	def display_quiz_question(A):
		f='multiple_choice';U='False';R='True';A.quiz_feedback_label.config(text=H)
		for M in A.quiz_option_buttons:M.destroy()
		A.quiz_option_buttons=[];A.quiz_next_button.config(state=C.DISABLED)
		if A.incorrectly_answered_words:A.current_quiz_word=A.incorrectly_answered_words.pop(0)
		elif A.quiz_words_to_ask:A.current_quiz_word=A.quiz_words_to_ask.pop(0)
		else:F.showinfo('测验结束','恭喜！所有题目都已答对！',parent=A.master);A.show_main_page();return
		g=re.sub(AI,H,A.current_quiz_word.get(D,H)).strip();A.speak_word(g);h=e.choice([f,'true_false']);E=[];G=H;i=A.settings[K];V=A.vocabulary_data.get(i,[])
		if h==f:
			P=f"请选择与 '{A.current_quiz_word.get(T,AC)}' 对应的单词：";G=A.current_quiz_word.get(D);E.append(G);W=[A for A in A.current_quiz_word.get(S,[])if A!=G];e.shuffle(W);X=[A[D]for A in V if A[D]!=G];e.shuffle(X)
			for Y in W:
				if I(E)<4 and Y not in E:E.append(Y)
			for Z in X:
				if I(E)<4 and Z not in E:E.append(Z)
			while I(E)<4:E.append(f"选项 {I(E)+1}")
			e.shuffle(E);A.current_quiz_correct_answer=G;A.quiz_question_label.config(text=P)
			for N in A1(4):M=B.Button(A.quiz_options_frame,text=E[N],style=r,command=lambda i=N:A.check_quiz_answer(A.quiz_option_buttons[i][AL]));M.grid(row=N//2,column=N%2,padx=10,pady=10,sticky=O);A.quiz_option_buttons.append(M)
		else:
			j=A.current_quiz_word.get(D,x);a=A.current_quiz_word.get(T,AC);k=e.choice([J,L])
			if k:Q=a;A.current_quiz_correct_answer=R
			else:
				b=[A[T]for A in V if A[T]!=a and A[T]!=AC]
				if b:Q=e.choice(b)
				else:Q='一个不正确的解释'
				A.current_quiz_correct_answer=U
			P=f"'{j}' 的意思是 '{Q}'，这个说法对吗？";A.quiz_question_label.config(text=P);c=B.Button(A.quiz_options_frame,text=R,style=r,command=lambda:A.check_quiz_answer(R));c.grid(row=0,column=0,padx=10,pady=10,sticky=O);A.quiz_option_buttons.append(c);d=B.Button(A.quiz_options_frame,text=U,style=r,command=lambda:A.check_quiz_answer(U));d.grid(row=0,column=1,padx=10,pady=10,sticky=O);A.quiz_option_buttons.append(d)
	def check_quiz_answer(A,selected_answer):
		F=selected_answer;G=F==A.current_quiz_correct_answer
		if G:A.quiz_feedback_label.config(text='正确！',foreground='green');A.quiz_items_completed+=1
		else:
			A.quiz_feedback_label.config(text=f"错误！正确答案是: {A.current_quiz_correct_answer}",foreground='red')
			if A.current_quiz_word not in A.incorrectly_answered_words:A.incorrectly_answered_words.append(A.current_quiz_word)
		J=A.current_quiz_word.get(D);E=A.settings[K]
		if E and E in A.vocabulary_data:
			for(H,I)in AP(A.vocabulary_data[E]):
				if I.get(D)==J:A.vocabulary_data[E][H][X]=I.get(X,0)+1;A.vocabulary_data[E][H][n]=z.now().isoformat();break
		A.save_progress();A.progress_bar.config(value=A.quiz_items_completed)
		for B in A.quiz_option_buttons:
			B.config(state=C.DISABLED)
			if B[AL]==A.current_quiz_correct_answer:B.config(style=AE)
			elif B[AL]==F and not G:B.config(style=AF)
			else:B.config(style=r)
		A.quiz_next_button.config(state=C.NORMAL)
	def next_quiz_question(A):A.display_quiz_question()
	def open_settings(A):
		d='跟随全局字体';I=C.Toplevel(A.master);I.title('设置');I.geometry('500x550');I.resizable(L,L);I.transient(A.master);I.grab_set();I.focus_set();u=A.settings[R]
		if u==A9:I.config(bg=w)
		elif u==AA:I.config(bg=v)
		elif A0 and A0.isDark():I.config(bg=w)
		else:I.config(bg=v)
		A.original_settings=copy.deepcopy(A.settings);A.settings_changed=L
		def H(*B):A.settings_changed=J
		X=B.Notebook(I);X.pack(pady=10,padx=10,fill=C.BOTH,expand=J);T=B.Frame(X,padding=s);X.add(T,text='显示设置');G=B.Frame(X,padding=s);X.add(G,text='字体设置');V=B.Frame(X,padding=s);X.add(V,text='语音设置');e=sorted(g(font.families()));f=[d]+e;K=0;B.Label(T,text='解释提示样式:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.reveal_hint_style_var=C.StringVar(value=A.settings[U])
		if A.settings[U]==AJ:A.reveal_hint_style_var.set(AM)
		elif A.settings[U]==m:A.reveal_hint_style_var.set('低调')
		elif A.settings[U]==AK:A.reveal_hint_style_var.set('明显')
		y=[AM,'低调','明显'];z=B.Combobox(T,textvariable=A.reveal_hint_style_var,values=y,state=W);z.grid(row=K,column=1,padx=5,pady=5,sticky=O);A.reveal_hint_style_var.trace_add(N,H);K+=1;B.Label(T,text='学习概述:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.show_session_summary_var=C.BooleanVar(value=A.settings[Q]);B.Checkbutton(T,text='显示学习内容概述',variable=A.show_session_summary_var).grid(row=K,column=1,padx=5,pady=5,sticky=D);A.show_session_summary_var.trace_add(N,H);K+=1;B.Label(T,text='日语罗马音:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var=C.BooleanVar(value=A.settings[k]);B.Checkbutton(T,text='显示日语假名罗马音',variable=A.show_romaji_for_kana_var).grid(row=K,column=1,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var.trace_add(N,H);K+=1;B.Label(T,text='暗色模式:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.dark_mode_var=C.StringVar(value=A.settings[R])
		if A.settings[R]==q:A.dark_mode_var.set(AN)
		elif A.settings[R]==A9:A.dark_mode_var.set('开启')
		elif A.settings[R]==AA:A.dark_mode_var.set('关闭')
		A1=[AN,'开启','关闭'];A2=B.Combobox(T,textvariable=A.dark_mode_var,values=A1,state=W);A2.grid(row=K,column=1,padx=5,pady=5,sticky=O);A.dark_mode_var.trace_add(N,H);K+=1;T.grid_columnconfigure(1,weight=1);F=0;B.Label(G,text='全局界面字体:').grid(row=F,column=0,padx=5,pady=5,sticky=D);A.global_font_family_var=C.StringVar(value=A.settings[P]);A3=B.Combobox(G,textvariable=A.global_font_family_var,values=e,state=W);A3.grid(row=F,column=1,padx=5,pady=5,sticky=O);A.global_font_family_var.trace_add(N,H);F+=1;B.Label(G,text='备用字体:').grid(row=F,column=0,padx=5,pady=5,sticky=D);A.fallback_font_family_var=C.StringVar(value=A.settings[p]);A4=B.Combobox(G,textvariable=A.fallback_font_family_var,values=e,state=W);A4.grid(row=F,column=1,padx=5,pady=5,sticky=O);A.fallback_font_family_var.trace_add(N,H);F+=1;B.Label(G,text='主单词字体:').grid(row=F,column=0,padx=5,pady=5,sticky=D);n=A.settings[Y]
		if n==E or n==A.settings[P]:A.main_word_font_family_var=C.StringVar(value=d)
		else:A.main_word_font_family_var=C.StringVar(value=n)
		A5=B.Combobox(G,textvariable=A.main_word_font_family_var,values=f,state=W);A5.grid(row=F,column=1,padx=5,pady=5,sticky=O);A.main_word_font_family_var.trace_add(N,H);F+=1;B.Label(G,text='主单词大小:').grid(row=F,column=0,padx=5,pady=5,sticky=D);A.main_word_font_size_var=C.StringVar(value=str(A.settings[h]));A6=B.Spinbox(G,from_=10,to_=72,textvariable=A.main_word_font_size_var,width=5);A6.grid(row=F,column=1,padx=5,pady=5,sticky=D);A.main_word_font_size_var.trace_add(N,H);F+=1;B.Label(G,text='括号文字字体:').grid(row=F,column=0,padx=5,pady=5,sticky=D);o=A.settings[Z]
		if o==E or o==A.settings[P]:A.bracketed_font_family_var=C.StringVar(value=d)
		else:A.bracketed_font_family_var=C.StringVar(value=o)
		A7=B.Combobox(G,textvariable=A.bracketed_font_family_var,values=f,state=W);A7.grid(row=F,column=1,padx=5,pady=5,sticky=O);A.bracketed_font_family_var.trace_add(N,H);F+=1;B.Label(G,text='括号文字大小:').grid(row=F,column=0,padx=5,pady=5,sticky=D);A.bracketed_font_size_var=C.StringVar(value=str(A.settings[i]));A8=B.Spinbox(G,from_=8,to_=48,textvariable=A.bracketed_font_size_var,width=5);A8.grid(row=F,column=1,padx=5,pady=5,sticky=D);A.bracketed_font_size_var.trace_add(N,H);F+=1;B.Label(G,text='罗马音字体:').grid(row=F,column=0,padx=5,pady=5,sticky=D);r=A.settings[a]
		if r==E or r==A.settings[P]:A.romaji_font_family_var=C.StringVar(value=d)
		else:A.romaji_font_family_var=C.StringVar(value=r)
		AB=B.Combobox(G,textvariable=A.romaji_font_family_var,values=f,state=W);AB.grid(row=F,column=1,padx=5,pady=5,sticky=O);A.romaji_font_family_var.trace_add(N,H);F+=1;B.Label(G,text='罗马音大小:').grid(row=F,column=0,padx=5,pady=5,sticky=D);A.romaji_font_size_var=C.StringVar(value=str(A.settings[j]));AC=B.Spinbox(G,from_=8,to_=48,textvariable=A.romaji_font_size_var,width=5);AC.grid(row=F,column=1,padx=5,pady=5,sticky=D);A.romaji_font_size_var.trace_add(N,H);F+=1;G.grid_columnconfigure(1,weight=1);S=0;B.Label(V,text='启用语音朗读:').grid(row=S,column=0,padx=5,pady=5,sticky=D);A.enable_tts_var=C.BooleanVar(value=A.settings[l]);B.Checkbutton(V,text='开启语音朗读',variable=A.enable_tts_var).grid(row=S,column=1,padx=5,pady=5,sticky=D);A.enable_tts_var.trace_add(N,H);S+=1;B.Label(V,text='选择语音:').grid(row=S,column=0,padx=5,pady=5,sticky=D);AD=[A.name for A in A.tts_voices];A.tts_voice_id_var=C.StringVar()
		if A.settings[M]and any(B.id==A.settings[M]for B in A.tts_voices):
			for x in A.tts_voices:
				if x.id==A.settings[M]:A.tts_voice_id_var.set(x.name);break
		elif A.tts_voices:A.tts_voice_id_var.set(A.tts_voices[0].name)
		AE=B.Combobox(V,textvariable=A.tts_voice_id_var,values=AD,state=W);AE.grid(row=S,column=1,padx=5,pady=5,sticky=O);A.tts_voice_id_var.trace_add(N,H);S+=1;B.Label(V,text='音量:').grid(row=S,column=0,padx=5,pady=5,sticky=D);A.tts_volume_var=C.DoubleVar(value=A.settings[b]);AF=B.Scale(V,from_=.0,to=t,orient=AZ,variable=A.tts_volume_var,command=lambda s:H());AF.grid(row=S,column=1,padx=5,pady=5,sticky=O);S+=1;B.Label(V,text='语速:').grid(row=S,column=0,padx=5,pady=5,sticky=D);A.tts_rate_var=C.IntVar(value=A.settings[c]);AG=B.Spinbox(V,from_=50,to_=300,textvariable=A.tts_rate_var,width=5);AG.grid(row=S,column=1,padx=5,pady=5,sticky=D);A.tts_rate_var.trace_add(N,H);S+=1;V.grid_columnconfigure(1,weight=1);B.Button(I,text='保存设置',command=lambda:A.save_settings(I)).pack(pady=10);I.protocol(AQ,lambda:A.confirm_close_settings(I))
	def confirm_close_settings(A,settings_window):
		B=settings_window
		if A.settings_changed:C=F.askyesnocancel('未保存的更改','您有未保存的设置。是否保存更改？',icon='warning',parent=B)
		else:A.on_settings_close(B)
	def on_settings_close(B,settings_window):A=settings_window;A.grab_release();A.destroy()
	def on_app_close(A):
		if A.tts_engine:
			try:A.tts_engine.stop()
			except f as B:A7(f"Error stopping TTS engine on app close: {B}")
		A.save_progress();A.master.destroy()
	def save_settings(A,settings_window):
		B=settings_window
		try:
			I={AM:AJ,'低调':m,'明显':AK};A.settings[U]=I[A.reveal_hint_style_var.get()];J={AN:q,'开启':A9,'关闭':AA};A.settings[R]=J[A.dark_mode_var.get()];A.settings[P]=A.global_font_family_var.get();A.settings[p]=A.fallback_font_family_var.get();C=A.main_word_font_family_var.get()
			if C==E:A.settings[Y]=E
			else:A.settings[Y]=C
			A.settings[h]=int(A.main_word_font_size_var.get());D=A.bracketed_font_family_var.get()
			if D==E:A.settings[Z]=E
			else:A.settings[Z]=D
			A.settings[i]=int(A.bracketed_font_size_var.get());G=A.romaji_font_family_var.get()
			if G==E:A.settings[a]=E
			else:A.settings[a]=G
			A.settings[j]=int(A.romaji_font_size_var.get());A.settings[l]=A.enable_tts_var.get();K=A.tts_voice_id_var.get()
			for H in A.tts_voices:
				if H.name==K:A.settings[M]=H.id;break
			A.settings[b]=A.tts_volume_var.get();A.settings[c]=A.tts_rate_var.get()
			if A.tts_engine:
				if A.settings[M]:A.tts_engine.setProperty(A4,A.settings[M])
				A.tts_engine.setProperty(AR,A.settings[b]);A.tts_engine.setProperty('rate',A.settings[c])
			A.settings[Q]=A.show_session_summary_var.get();A.settings[k]=A.show_romaji_for_kana_var.get();A.save_progress();A.setup_styles();A.settings_changed=L;F.showinfo('设置','设置已保存！',parent=B);A.on_settings_close(B)
		except AD:F.showerror(o,'字体大小、音量或语速必须是有效数字！',parent=B)
		except f as N:F.showerror(o,f"保存设置时发生错误: {N}",parent=B)
if __name__=='__main__':A=C.Tk();Ah=Ag(A);A.mainloop()