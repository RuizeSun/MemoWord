Ab='settings'
Aa='session_start_count'
AZ='direct'
AY='horizontal'
AX='QuizFeedback.TLabel'
AW='QuizQuestion.TLabel'
AV='LearningRomaji.TLabel'
AU='LearningBracketed.TLabel'
AT='LearningSimilar.TLabel'
AS='LearningDefinition.TLabel'
AR='LearningWord.TLabel'
AQ='volume'
AP='WM_DELETE_WINDOW'
AO=enumerate
AN=ImportError
AM='跟随系统设置'
AL='不显示'
AK='text'
AJ='Obvious'
AI='None'
AH='〔.*?〕'
AG='N/A'
AF='vocabulary_data'
AE='utf-8'
AD='Incorrect.QuizOption.TButton'
AC='Correct.QuizOption.TButton'
AB=ValueError
AA='无解释'
A9='开始学习'
A8='Off'
A7='On'
A6='black'
A5='Arial'
A4='Helvetica'
A3=print
A1='跟随全局字体'
A0='bold'
z='#2b2b2b'
y='#f0f0f0'
x='voice'
w=1.
v=range
q='System'
p='fallback_font_family'
o=list
n='错误'
m='15'
l='QuizOption.TButton'
k='Subtle'
j='enable_tts'
i='show_romaji_for_kana'
h='romaji_font_size'
g='bracketed_font_size'
f='main_word_font_size'
e='last_study_time'
d='tts_rate'
c='tts_volume'
b='romaji_font_family'
a='bracketed_font_family'
Z='main_word_font_family'
Y=Exception
W='center'
V='study_count'
U='readonly'
T='reveal_hint_style'
Q='i'
S='dark_mode'
R='show_session_summary'
P='d'
M='o'
O='global_font_family'
N='ew'
L=None
K=False
J='tts_voice_id'
I=True
H=len
G=''
F='FollowGlobal'
D='w'
import tkinter as C
from tkinter import ttk as B,filedialog as Ac,messagebox as E,font
import json as r
from datetime import datetime as s,timedelta as Ad
import os,random as X,re as t,copy,threading as Ae,queue
try:import darkdetect as u
except AN:u=L
try:import pyttsx3 as A2
except AN:A2=L
class Af:
	def __init__(A,master):z='ttsu';y='cchi';x='tta';v='sso';u='sse';t='ssu';s='sshi';r='ssa';o='kko';n='kke';m='kku';l='kki';e='kka';Y='mmi';X='ru';W='zu';V='ji';U='yo';P='yu';N='ya';H='ka';G='u';E='a';D=master;C='e';B='wa';A.master=D;D.title('MemoWord - 记单词');D.geometry('800x600');D.minsize(600,400);A.vocabulary_data=[];A.progress_file='memoword_progress.json';A.session_start_count=0;A.settings={O:A4,p:A5,Z:F,f:36,a:F,g:20,b:F,h:14,T:k,R:I,i:K,S:q,j:K,J:L,c:w,d:175};A.direct_learning_session=[];A.direct_word_index=0;A.quiz_session_words=[];A.quiz_words_to_ask=[];A.incorrectly_answered_words=[];A.current_quiz_word=L;A.current_quiz_correct_answer=L;A.quiz_items_completed=0;A.quiz_total_items_to_complete=0;A.recently_learned_for_quiz=[];A.KANA_TO_ROMAJI_MAP={'っか':e,'っき':l,'っく':m,'っけ':n,'っこ':o,'っさ':r,'っし':s,'っす':t,'っせ':u,'っそ':v,'った':x,'っち':y,'っつ':z,'って':'tte','っと':'tto','っぱ':'ppa','っぴ':'ppi','っぷ':'ppu','っぺ':'ppe','っぽ':'ppo','っは':'hha','っひ':'hhi','っふ':'ffu','っへ':'hhe','っほ':'hho','っま':'mma','っみ':Y,'っむ':'mmu','っめ':'mme','っも':'mmo','っや':'yya','っゆ':'yyu','っよ':'yyo','っら':'rra','っり':'rri','っる':'rru','っれ':'rre','っろ':'rro','っわ':'wwa','ッか':e,'ッキ':l,'ック':m,'ッケ':n,'ッコ':o,'ッサ':r,'ッシ':s,'ッス':t,'ッセ':u,'ッソ':v,'ッタ':x,'ッチ':y,'ッツ':z,'ッテ':'tte','ット':'tto','ッパ':'ppa','ッピ':'ppi','ップ':'ppu','ッペ':'ppe','ッポ':'ppo','ッハ':'hha','ッヒ':'hhi','ッフ':'ffu','ッヘ':'hhe','ッホ':'hho','ッマ':'mma','ッミ':Y,'ッム':'mmu','ッメ':'mme','ッモ':'mmo','ッヤ':'yya','ッユ':'yyu','ッヨ':'yyo','ッラ':'rra','ッリ':'rri','ッル':'rru','ッレ':'rre','ッロ':'rro','ッワ':'wwa','きゃ':'kya','きゅ':'kyu','きょ':'kyo','しゃ':'sha','しゅ':'shu','しょ':'sho','ちゃ':'cha','ちゅ':'chu','ちょ':'cho','にゃ':'nya','にゅ':'nyu','にょ':'nyo','ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','みゃ':'mya','みゅ':'myu','みょ':'myo','りゃ':'rya','りゅ':'ryu','りょ':'ryo','ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo','じゃ':'ja','じゅ':'ju','じょ':'jo','びゃ':'bya','びゅ':'byu','びょ':'byo','ぴゃ':'pya','ぴゅ':'pyu','ぴょ':'pyo','キャ':'kya','キュ':'kyu','キョ':'kyo','シャ':'sha','シュ':'shu','ショ':'sho','チャ':'cha','チュ':'chu','チョ':'cho','ニャ':'nya','ニュ':'nyu','ニョ':'nyo','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','ミャ':'mya','ミュ':'myu','ミョ':'myo','リャ':'rya','リュ':'ryu','リョ':'ryo','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ジャ':'ja','ジュ':'ju','ジョ':'jo','ビャ':'bya','ビュ':'byu','ビョ':'byo','ピャ':'pya','ピュ':'pyu','ピョ':'pyo','ああ':'aa','いい':'ii','うう':'uu','ええ':'ee','おお':'oo','おう':'oo','ー':'-','は':B,'へ':C,'を':M,'あ':E,'い':Q,'う':G,'え':C,'お':M,'か':H,'き':'ki','く':'ku','け':'ke','こ':'ko','さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to','な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':N,'ゆ':P,'よ':U,'ら':'ra','り':'ri',X:X,'れ':'re','ろ':'ro','わ':B,'ゐ':'wi','ゑ':'we','を':'wo','ん':'n','が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ざ':'za','じ':V,'ず':W,'ぜ':'ze','ぞ':'zo','だ':'da','ぢ':V,'づ':W,'で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ア':E,'イ':Q,'ウ':G,'エ':C,'オ':M,'カ':H,'キ':'ki','ク':'ku','ケ':'ke','コ':'ko','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','マ':'ma','ミ':Y,'ム':'mu','メ':'me','モ':'mo','ヤ':N,'ユ':P,'ヨ':U,'ラ':'ra','リ':'ri','ル':X,'レ':'re','ロ':'ro','ワ':B,'ヰ':'wi','ヱ':'we','ヲ':'wo','ン':'n','ガ':'ga','ギ':'gi','グ':'gu','ゲ':'ge','ゴ':'go','ザ':'za','ジ':V,'ズ':W,'ゼ':'ze','ゾ':'zo','ダ':'da','ヂ':V,'ヅ':W,'デ':'de','ド':'do','バ':'ba','ビ':'bi','ブ':'bu','ベ':'be','ボ':'bo','パ':'pa','ピ':'pi','プ':'pu','ぺ':'pe','ポ':'po','ぁ':E,'ぃ':Q,'ぅ':G,'ぇ':C,'ぉ':M,'ァ':E,'ィ':Q,'ゥ':G,'ェ':C,'ォ':M,'ゃ':N,'ゅ':P,'ょ':U,'ャ':N,'ュ':P,'ョ':U,'ゎ':B,'ヮ':B,'ヶ':H,'ヵ':H};A.tts_engine=L;A.tts_voices=[];A.tts_thread=L;A.setup_tts();A.setup_styles();A.create_widgets();A.load_initial_data();A.master.protocol(AP,A.on_app_close)
	def setup_tts(A):
		if A2 and not A.tts_engine:
			try:
				A.tts_engine=A2.init();A.tts_voices=A.tts_engine.getProperty('voices')
				if A.settings[J]and any(B.id==A.settings[J]for B in A.tts_voices):A.tts_engine.setProperty(x,A.settings[J])
				else:
					C=K
					for B in A.tts_voices:
						if'zh'in B.languages or'ZH'in B.id:A.settings[J]=B.id;A.tts_engine.setProperty(x,B.id);C=I;break
					if not C:
						for B in A.tts_voices:
							if'en'in B.languages or'EN'in B.id:A.settings[J]=B.id;A.tts_engine.setProperty(x,B.id);C=I;break
					if not C and A.tts_voices:A.settings[J]=A.tts_voices[0].id;A.tts_engine.setProperty(x,A.tts_voices[0].id)
				A.tts_engine.setProperty(AQ,A.settings[c]);A.tts_engine.setProperty('rate',A.settings[d])
				if not A.tts_thread or not A.tts_thread.is_alive():A.tts_thread=Ae.Thread(target=A._tts_run_loop,daemon=I);A.tts_thread.start()
			except Y as D:E.showwarning('TTS 初始化失败',f"无法初始化文字转语音功能：{D}\n请确保已安装必要的语音包。",parent=A.master);A.tts_engine=L
		elif not A2:E.showwarning('TTS 库未安装',"pyttsx3 库未安装。文字转语音功能将不可用。\n请运行 'pip install pyttsx3' 进行安装。",parent=A.master)
	def _tts_run_loop(A):
		if A.tts_engine:
			try:A.tts_engine.runAndWait()
			except Y as B:A3(f"TTS引擎运行错误: {B}")
	def speak_word(A,text):
		if A.settings[j]and A.tts_engine:
			try:A.tts_engine.stop();A.tts_engine.say(text)
			except Y as B:A3(f"TTS say error: {B}")
	def setup_styles(G):
		AL='!readonly';AK='TCombobox';AJ='Treeview';AI='TButton';AH='#5a5a5a';AG='#87ceeb';AF='#555555';AE='#a8d8ff';AB='#0056b3';AA='bg_checkbutton';A9='fg_hint_obvious';A5='fg_hint_subtle';A1='#3c3c3c';x='bg_spinbox_field';w='fg_combobox_arrow';v='bg_selected_treeview';t='fg_romaji';s='fg_incorrect_button';r='fg_correct_button';q='fg_quiz_question';p='fg_learning_word';o='fg_treeview_heading';n='bg_treeview_heading';m='fg_treeview';k='bg_treeview';d='#ffffff';c='fg_combobox_text';Y='fg_similar_words';X='bg_frame';W='bg_combobox_selected';V='bg_combobox_field';T='fg_active_button';R='bg_active_button';Q='bg_incorrect_button';P='bg_correct_button';N='fg_label';M='#333333';L='fg_button';K='!disabled';J='active';I='#e0e0e0';H='bg_button';E='bg_label';C=B.Style();C.theme_use('clam');A2={X:y,E:y,N:M,H:'#dddddd',L:M,k:d,m:M,n:I,o:M,p:AB,q:AB,P:'lightgreen',r:A6,Q:'salmon',s:A6,A5:'gray',A9:'blue',Y:'#666666',t:'#888888',AA:y,R:I,T:'#000000',v:AE,V:d,W:AE,c:M,w:M,x:d};A3={X:z,E:z,N:I,H:'#444444',L:I,k:A1,m:I,n:AF,o:I,p:AG,q:AG,P:'#4CAF50',r:'white',Q:'#FF6347',s:'white',A5:'#aaaaaa',A9:'#add8e6',Y:'#bbbbbb',t:'#cccccc',AA:z,R:AF,T:d,v:AH,V:A1,W:AH,c:I,w:I,x:A1};A4=G.settings[S]
		if A4==A7:A=A3
		elif A4==A8:A=A2
		elif u and u.isDark():A=A3
		else:A=A2
		D=G.settings[O];e=G.settings[Z]
		if e==F:e=D
		i=G.settings[a]
		if i==F:i=D
		j=G.settings[b]
		if j==F:j=D
		C.configure('TFrame',background=A[X]);C.configure('TLabel',background=A[E],foreground=A[N],font=(D,10));C.configure(AI,font=(D,10),padding=6,background=A[H],foreground=A[L]);C.map(AI,background=[(J,A[R]),(K,A[H])],foreground=[(J,A[T]),(K,A[L])]);C.configure('Treeview.Heading',font=(D,10,A0),background=A[n],foreground=A[o]);C.configure(AJ,font=(D,10),rowheight=25,background=A[k],foreground=A[m]);C.map(AJ,background=[('selected',A[v])]);C.configure(AR,font=(e,G.settings[f],A0),foreground=A[p],background=A[E]);C.configure(AS,font=(D,18),foreground=A[N],background=A[E]);C.configure(AT,font=(D,12),foreground=A[Y],background=A[E]);C.configure(AU,font=(i,G.settings[g]),foreground=A[Y],background=A[E]);C.configure(AV,font=(j,G.settings[h]),foreground=A[t],background=A[E]);C.configure(AW,font=(D,20,A0),foreground=A[q],background=A[E],wraplength=700);C.configure(l,font=(D,14),padding=10,background=A[H],foreground=A[L]);C.map(l,background=[(J,A[R]),(K,A[H])],foreground=[(J,A[T]),(K,A[L])]);C.configure(AX,font=(D,14,A0),background=A[E]);C.configure(AC,background=A[P],foreground=A[r]);C.map(AC,background=[(J,A[P]),(K,A[P])]);C.configure(AD,background=A[Q],foreground=A[s]);C.map(AD,background=[(J,A[Q]),(K,A[Q])]);C.configure('TCheckbutton',background=A[E],foreground=A[N],font=(D,10));C.configure(AK,font=(D,10),fieldbackground=A[V],selectbackground=A[W],background=A[H],foreground=A[c],arrowcolor=A[w]);C.map(AK,fieldbackground=[(U,A[V]),(AL,A[V])],selectbackground=[(U,A[W]),(AL,A[W])],background=[(J,A[R]),(K,A[H])],foreground=[(J,A[T]),(K,A[L])]);C.configure('TSpinbox',font=(D,10),fieldbackground=A[x],foreground=A[c]);G.master.config(bg=A[X])
	def create_widgets(A):A.main_frame=B.Frame(A.master,padding=m);A.main_frame.pack(fill=C.BOTH,expand=I);A.learning_frame=B.Frame(A.master,padding=m);A.progress_bar=B.Progressbar(A.learning_frame,orient=AY,mode='determinate');A.progress_bar.pack(fill=C.X,pady=5);A.create_main_page_widgets();A.create_direct_learning_widgets();A.create_quiz_widgets()
	def create_main_page_widgets(A):G='definition';F='word';B.Label(A.main_frame,text='MemoWord 词汇表',font=(A.settings[O],18,A0)).pack(pady=15);A.total_study_label=B.Label(A.main_frame,text='进入学习界面次数: 0',font=(A.settings[O],12));A.total_study_label.pack(pady=5);A.vocab_tree=B.Treeview(A.main_frame,columns=(F,G,V,e),show='headings');A.vocab_tree.heading(F,text='词汇');A.vocab_tree.heading(G,text='解释');A.vocab_tree.heading(V,text='学习次数');A.vocab_tree.heading(e,text='上次学习时间');A.vocab_tree.column(F,width=150,minwidth=100,anchor=W);A.vocab_tree.column(G,width=300,minwidth=200,anchor=D);A.vocab_tree.column(V,width=100,minwidth=80,anchor=W);A.vocab_tree.column(e,width=150,minwidth=120,anchor=W);A.vocab_tree.pack(fill=C.BOTH,expand=I,pady=10);H=B.Scrollbar(A.vocab_tree,orient='vertical',command=A.vocab_tree.yview);H.pack(side='right',fill='y');A.vocab_tree.configure(yscrollcommand=H.set);E=B.Frame(A.main_frame);E.pack(pady=15);A.import_button=B.Button(E,text='导入词汇表',command=A.load_vocabulary);A.import_button.pack(side=C.LEFT,padx=10);A.start_learning_button=B.Button(E,text=A9,command=A.start_learning);A.start_learning_button.pack(side=C.LEFT,padx=10);A.settings_button=B.Button(E,text='设置',command=A.open_settings);A.settings_button.pack(side=C.LEFT,padx=10)
	def create_direct_learning_widgets(A):A.direct_learning_sub_frame=B.Frame(A.learning_frame,padding=m);A.learning_romaji_label=B.Label(A.direct_learning_sub_frame,text=G,style=AV,wraplength=700,anchor=W);A.learning_romaji_label.pack(pady=(20,0),fill=C.X);A.learning_word_label=B.Label(A.direct_learning_sub_frame,text=G,style=AR,wraplength=700,anchor=W);A.learning_word_label.pack(pady=(5,0),fill=C.X);A.learning_bracketed_label=B.Label(A.direct_learning_sub_frame,text=G,style=AU,wraplength=700,anchor=W);A.learning_bracketed_label.pack(pady=(5,20),fill=C.X);A.learning_definition_label=B.Label(A.direct_learning_sub_frame,text=G,style=AS,wraplength=700,anchor=W);A.learning_definition_label.pack(pady=20,fill=C.X);A.learning_similar_label=B.Label(A.direct_learning_sub_frame,text=G,style=AT,wraplength=700,anchor=W);A.learning_similar_label.pack(pady=10,fill=C.X);D=B.Frame(A.direct_learning_sub_frame);D.pack(pady=30);A.reveal_button=B.Button(D,text='显示解释',command=A.reveal_definition);A.reveal_button.pack(side=C.LEFT,padx=15);A.next_word_button=B.Button(D,text='下一个',command=A.next_direct_word,state=C.DISABLED);A.next_word_button.pack(side=C.LEFT,padx=15);A.back_to_main_button_direct=B.Button(A.direct_learning_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_direct.pack(pady=20)
	def create_quiz_widgets(A):
		A.quiz_sub_frame=B.Frame(A.learning_frame,padding=m);A.quiz_question_label=B.Label(A.quiz_sub_frame,text=G,style=AW,anchor=W);A.quiz_question_label.pack(pady=40,fill=C.X);A.quiz_options_frame=B.Frame(A.quiz_sub_frame);A.quiz_options_frame.pack(pady=20,fill=C.X,expand=I);A.quiz_options_frame.grid_columnconfigure(0,weight=1);A.quiz_options_frame.grid_columnconfigure(1,weight=1);A.quiz_option_buttons=[]
		for D in v(4):E=B.Button(A.quiz_options_frame,text=f"Option {D+1}",style=l);E.grid(row=D//2,column=D%2,padx=10,pady=10,sticky=N);A.quiz_option_buttons.append(E);E.grid_forget()
		A.quiz_feedback_label=B.Label(A.quiz_sub_frame,text=G,style=AX);A.quiz_feedback_label.pack(pady=15);A.quiz_next_button=B.Button(A.quiz_sub_frame,text='下一个问题',command=A.next_quiz_question,state=C.DISABLED);A.quiz_next_button.pack(pady=10);A.back_to_main_button_quiz=B.Button(A.quiz_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_quiz.pack(pady=20)
	def show_main_page(A):A.learning_frame.pack_forget();A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack_forget();A.main_frame.pack(fill=C.BOTH,expand=I);A.update_main_page_display()
	def show_learning_page(A,mode):
		A.main_frame.pack_forget();A.learning_frame.pack(fill=C.BOTH,expand=I);A.progress_bar.config(value=0)
		if mode==AZ:A.quiz_sub_frame.pack_forget();A.direct_learning_sub_frame.pack(fill=C.BOTH,expand=I)
		elif mode=='quiz':A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack(fill=C.BOTH,expand=I)
	def load_initial_data(A):A.load_progress();A.update_main_page_display()
	def load_vocabulary(A):
		N=Ac.askopenfilename(filetypes=[('JSON files','*.json')])
		if not N:return
		try:
			with open(N,'r',encoding=AE)as U:O=r.load(U)
			J={A[D]:A for A in A.vocabulary_data};K=[]
			for B in O:
				F=B.get(D)
				if not F:continue
				if F in J:C=J[F];C[P]=B.get(P,C.get(P,G));C[M]=B.get(M,C.get(M,[]));C[Q]=B.get(Q,C.get(Q,0));K.append(C)
				else:K.append({Q:B.get(Q,0),D:F,P:B.get(P,G),M:B.get(M,[]),V:0,e:L})
			I={}
			for R in K:I[R[D]]=R
			for(S,W)in J.items():
				if S not in I:I[S]=W
			A.vocabulary_data=o(I.values());A.vocabulary_data.sort(key=lambda x:x.get(Q,0));A.save_progress();A.update_main_page_display();E.showinfo('导入成功',f"成功导入 {H(O)} 个词汇。",parent=A.master)
		except r.JSONDecodeError:E.showerror(n,'无效的JSON文件格式。请确保文件内容符合JSON规范。',parent=A.master)
		except Y as T:E.showerror(n,f"导入词汇时发生错误: {T}",parent=A.master);A3(f"Error during import: {T}")
		finally:A.master.focus_set()
	def load_progress(A):
		if os.path.exists(A.progress_file):
			try:
				with open(A.progress_file,'r',encoding=AE)as C:
					B=r.load(C)
					if isinstance(B,dict)and AF in B:A.vocabulary_data=B.get(AF,[]);A.session_start_count=B.get(Aa,0);A.settings.update(B.get(Ab,{}))
					else:A.vocabulary_data=B;A.session_start_count=0
			except r.JSONDecodeError:E.showerror(n,'学习进度文件损坏或格式不正确，将重新创建。',parent=A.master);A.vocabulary_data=[];A.session_start_count=0;A.settings={O:A4,p:A5,Z:F,f:36,a:F,g:20,b:F,h:14,T:k,R:I,i:K,S:q,j:K,J:L,c:w,d:175}
			except Y as D:E.showerror(n,f"加载学习进度时发生错误: {D}",parent=A.master);A.vocabulary_data=[];A.session_start_count=0;A.settings={O:A4,p:A5,Z:F,f:36,a:F,g:20,b:F,h:14,T:k,R:I,i:K,S:q,j:K,J:L,c:w,d:175}
		else:A.vocabulary_data=[];A.session_start_count=0;A.settings={O:A4,p:A5,Z:F,f:36,a:F,g:20,b:F,h:14,T:k,R:I,i:K,S:q,j:K,J:L,c:w,d:175}
	def save_progress(A):
		try:
			B={AF:A.vocabulary_data,Aa:A.session_start_count,Ab:A.settings}
			with open(A.progress_file,D,encoding=AE)as C:r.dump(B,C,ensure_ascii=K,indent=4)
		except Y as F:E.showerror(n,f"保存学习进度时发生错误: {F}",parent=A.master)
	def update_main_page_display(A):
		for H in A.vocab_tree.get_children():A.vocab_tree.delete(H)
		for B in A.vocabulary_data:
			I=B.get(D,AG);J=B.get(P,AG);K=B.get(V,0);F=B.get(e);E='未学习'
			if F:
				try:L=s.fromisoformat(F);E=L.strftime('%Y-%m-%d %H:%M')
				except AB:E='日期格式错误'
			A.vocab_tree.insert(G,C.END,values=(I,J,K,E))
		A.total_study_label.config(text=f"进入学习界面次数: {A.session_start_count}")
	def start_learning(A):
		if not A.vocabulary_data:E.showwarning('提示','请先导入词汇表！',parent=A.master);return
		A.session_start_count+=1;A.save_progress();D=[];C=[];F=[];J=s.now();K=J-Ad(days=3)
		for B in A.vocabulary_data:
			G=B.get(V,0);I=B.get(e)
			if G==0:D.append(B)
			elif I:
				try:
					L=s.fromisoformat(I)
					if G<15 and L<K:C.append(B)
					else:F.append(B)
				except AB:C.append(B)
			else:C.append(B)
		D.sort(key=lambda x:x.get(Q,0))
		if C:
			if A.settings[R]:E.showinfo(A9,f"有 {H(C)} 个单词需要优先复习！",parent=A.master)
			A.start_quiz_session(C)
		elif A.recently_learned_for_quiz:
			if A.settings[R]:E.showinfo('开始复习',f"开始复习刚刚学习的 {H(A.recently_learned_for_quiz)} 个单词！",parent=A.master)
			M=o(A.recently_learned_for_quiz);A.recently_learned_for_quiz.clear();A.start_quiz_session(M)
		elif D:
			A.direct_learning_session=D[:5]
			if A.settings[R]:E.showinfo(A9,f"开始学习 {H(A.direct_learning_session)} 个新单词！",parent=A.master)
			A.start_direct_learning_session()
		else:
			if not F:E.showinfo('恭喜','所有单词都已学习或复习完毕！',parent=A.master);return
			X.shuffle(F);A.quiz_session_words=F[:10]
			if A.settings[R]:E.showinfo(A9,f"开始复习 {H(A.quiz_session_words)} 个旧单词！",parent=A.master)
			A.start_quiz_session(A.quiz_session_words)
		A.master.focus_set()
	def start_direct_learning_session(A):
		A.direct_word_index=0
		if A.direct_learning_session:A.show_learning_page(AZ);A.progress_bar.config(maximum=H(A.direct_learning_session),value=0);A.display_current_direct_word()
		else:A.show_main_page()
	def _kana_to_romaji(E,kana_text):
		B=kana_text;C=[];A=0
		while A<H(B):
			M=K
			for J in v(3,0,-1):
				if A+J<=H(B):
					D=B[A:A+J]
					if D in E.KANA_TO_ROMAJI_MAP:
						if D=='ー'and C:
							N=t.search('[aeiou]$',C[-1])
							if N:C[-1]+=N.group(0)
							else:C.append('-')
						elif D in['ん','ン']and A+1<H(B)and t.match('[あいうえおやゆよアイウエオヤユヨ]',B[A+1]):C.append("n'")
						elif D in['っ','ッ']and A+1<H(B):
							F=L
							for O in v(3,0,-1):
								if A+1+O<=H(B):
									P=B[A+1:A+1+O]
									if P in E.KANA_TO_ROMAJI_MAP:F=E.KANA_TO_ROMAJI_MAP[P];break
							if F and F[0].isalpha():C.append(F[0])
						else:C.append(E.KANA_TO_ROMAJI_MAP[D])
						A+=J;M=I;break
			if not M:C.append(B[A]);A+=1
		return G.join(C)
	def display_current_direct_word(A):
		O="点击 '显示解释' 查看"
		if A.direct_word_index<H(A.direct_learning_session):
			I=A.direct_learning_session[A.direct_word_index];B=I.get(D,G);A.progress_bar.config(value=A.direct_word_index+1)
			if A.settings[i]:P=t.sub(AH,G,B);Q=G.join(A for A in P if'\u3040'<=A<='ゟ'or'゠'<=A<='ヿ'or A=='ー');S=A._kana_to_romaji(Q);A.learning_romaji_label.config(text=S)
			else:A.learning_romaji_label.config(text=G)
			J=t.search(AH,B)
			if J:K=J.group(0);L=B.replace(K,G).strip();A.learning_word_label.config(text=L);A.learning_bracketed_label.config(text=K)
			else:A.learning_word_label.config(text=B);A.learning_bracketed_label.config(text=G)
			F=A.settings[T]
			if F==AI:A.learning_definition_label.config(text=G,foreground=A6)
			elif F==k:A.learning_definition_label.config(text=O,foreground='gray')
			elif F==AJ:A.learning_definition_label.config(text=O,foreground='blue')
			N=', '.join(I.get(M,[]));A.learning_similar_label.config(text=f"形近/音近词: {N}"if N else'无形近/音近词');A.reveal_button.config(state=C.NORMAL);A.next_word_button.config(state=C.DISABLED);A.speak_word(L)
		elif A.direct_learning_session:
			A.recently_learned_for_quiz=o(A.direct_learning_session)
			if A.settings[R]:E.showinfo('学习完成',f"本次新词学习已完成！接下来将复习刚刚学习的 {H(A.recently_learned_for_quiz)} 个单词。",parent=A.master)
			A.start_quiz_session(A.recently_learned_for_quiz)
		else:E.showinfo('学习结束','本次学习已完成！',parent=A.master);A.show_main_page()
	def reveal_definition(A):
		if A.direct_word_index<H(A.direct_learning_session):
			B=A.direct_learning_session[A.direct_word_index];A.learning_definition_label.config(text=B.get(P,AA),foreground=A6);A.reveal_button.config(state=C.DISABLED);A.next_word_button.config(state=C.NORMAL);G=B.get(D)
			for(E,F)in AO(A.vocabulary_data):
				if F.get(D)==G:A.vocabulary_data[E][V]=F.get(V,0)+1;A.vocabulary_data[E][e]=s.now().isoformat();break
			A.save_progress()
	def next_direct_word(A):A.direct_word_index+=1;A.display_current_direct_word()
	def start_quiz_session(A,words_to_quiz_initial=L):
		C=words_to_quiz_initial;A.incorrectly_answered_words=[];A.quiz_items_completed=0;A.quiz_words_to_ask=[];B=[]
		if C is not L:B=o(C)
		else:B=o(A.quiz_session_words)
		for D in B:
			for F in v(3):A.quiz_words_to_ask.append(D)
		X.shuffle(A.quiz_words_to_ask);A.quiz_total_items_to_complete=H(A.quiz_words_to_ask)
		if A.quiz_words_to_ask:A.show_learning_page('quiz');A.progress_bar.config(maximum=A.quiz_total_items_to_complete,value=A.quiz_items_completed);A.display_quiz_question()
		else:E.showinfo('测验结束','本次测验已完成！',parent=A.master);A.show_main_page()
	def display_quiz_question(A):
		d='multiple_choice';T='False';S='True';A.quiz_feedback_label.config(text=G)
		for L in A.quiz_option_buttons:L.destroy()
		A.quiz_option_buttons=[];A.quiz_next_button.config(state=C.DISABLED)
		if A.incorrectly_answered_words:A.current_quiz_word=A.incorrectly_answered_words.pop(0)
		elif A.quiz_words_to_ask:A.current_quiz_word=A.quiz_words_to_ask.pop(0)
		else:E.showinfo('测验结束','恭喜！所有题目都已答对！',parent=A.master);A.show_main_page();return
		e=t.sub(AH,G,A.current_quiz_word.get(D,G)).strip();A.speak_word(e);f=X.choice([d,'true_false']);F=[];J=G
		if f==d:
			Q=f"请选择与 '{A.current_quiz_word.get(P,AA)}' 对应的单词：";J=A.current_quiz_word.get(D);F.append(J);U=[A for A in A.current_quiz_word.get(M,[])if A!=J];X.shuffle(U);V=[A[D]for A in A.vocabulary_data if A[D]!=J];X.shuffle(V)
			for W in U:
				if H(F)<4 and W not in F:F.append(W)
			for Y in V:
				if H(F)<4 and Y not in F:F.append(Y)
			while H(F)<4:F.append(f"选项 {H(F)+1}")
			X.shuffle(F);A.current_quiz_correct_answer=J;A.quiz_question_label.config(text=Q)
			for O in v(4):L=B.Button(A.quiz_options_frame,text=F[O],style=l,command=lambda i=O:A.check_quiz_answer(A.quiz_option_buttons[i][AK]));L.grid(row=O//2,column=O%2,padx=10,pady=10,sticky=N);A.quiz_option_buttons.append(L)
		else:
			g=A.current_quiz_word.get(D,AG);Z=A.current_quiz_word.get(P,AA);h=X.choice([I,K])
			if h:R=Z;A.current_quiz_correct_answer=S
			else:
				a=[A[P]for A in A.vocabulary_data if A[P]!=Z and A[P]!=AA]
				if a:R=X.choice(a)
				else:R='一个不正确的解释'
				A.current_quiz_correct_answer=T
			Q=f"'{g}' 的意思是 '{R}'，这个说法对吗？";A.quiz_question_label.config(text=Q);b=B.Button(A.quiz_options_frame,text=S,style=l,command=lambda:A.check_quiz_answer(S));b.grid(row=0,column=0,padx=10,pady=10,sticky=N);A.quiz_option_buttons.append(b);c=B.Button(A.quiz_options_frame,text=T,style=l,command=lambda:A.check_quiz_answer(T));c.grid(row=0,column=1,padx=10,pady=10,sticky=N);A.quiz_option_buttons.append(c)
	def check_quiz_answer(A,selected_answer):
		E=selected_answer;F=E==A.current_quiz_correct_answer
		if F:A.quiz_feedback_label.config(text='正确！',foreground='green');A.quiz_items_completed+=1
		else:
			A.quiz_feedback_label.config(text=f"错误！正确答案是: {A.current_quiz_correct_answer}",foreground='red')
			if A.current_quiz_word not in A.incorrectly_answered_words:A.incorrectly_answered_words.append(A.current_quiz_word)
		I=A.current_quiz_word.get(D)
		for(G,H)in AO(A.vocabulary_data):
			if H.get(D)==I:A.vocabulary_data[G][V]=H.get(V,0)+1;A.vocabulary_data[G][e]=s.now().isoformat();break
			A.save_progress()
		A.progress_bar.config(value=A.quiz_items_completed)
		for B in A.quiz_option_buttons:
			B.config(state=C.DISABLED)
			if B[AK]==A.current_quiz_correct_answer:B.config(style=AC)
			elif B[AK]==E and not F:B.config(style=AD)
			else:B.config(style=l)
		A.quiz_next_button.config(state=C.NORMAL)
	def next_quiz_question(A):A.display_quiz_question()
	def open_settings(A):
		M='write';L=C.Toplevel(A.master);L.title('设置');L.geometry('500x550');L.resizable(K,K);L.transient(A.master);L.grab_set();L.focus_set();s=A.settings[S]
		if s==A7:L.config(bg=z)
		elif s==A8:L.config(bg=y)
		elif u and u.isDark():L.config(bg=z)
		else:L.config(bg=y)
		A.original_settings=copy.deepcopy(A.settings);A.settings_changed=K
		def H(*B):A.settings_changed=I
		X=B.Notebook(L);X.pack(pady=10,padx=10,fill=C.BOTH,expand=I);V=B.Frame(X,padding=m);X.add(V,text='显示设置');G=B.Frame(X,padding=m);X.add(G,text='字体设置');W=B.Frame(X,padding=m);X.add(W,text='语音设置');Y=sorted(o(font.families()));e=[A1]+Y;P=0;B.Label(V,text='解释提示样式:').grid(row=P,column=0,padx=5,pady=5,sticky=D);A.reveal_hint_style_var=C.StringVar(value=A.settings[T])
		if A.settings[T]==AI:A.reveal_hint_style_var.set(AL)
		elif A.settings[T]==k:A.reveal_hint_style_var.set('低调')
		elif A.settings[T]==AJ:A.reveal_hint_style_var.set('明显')
		v=[AL,'低调','明显'];x=B.Combobox(V,textvariable=A.reveal_hint_style_var,values=v,state=U);x.grid(row=P,column=1,padx=5,pady=5,sticky=N);A.reveal_hint_style_var.trace_add(M,H);P+=1;B.Label(V,text='学习概述:').grid(row=P,column=0,padx=5,pady=5,sticky=D);A.show_session_summary_var=C.BooleanVar(value=A.settings[R]);B.Checkbutton(V,text='显示学习内容概述',variable=A.show_session_summary_var).grid(row=P,column=1,padx=5,pady=5,sticky=D);A.show_session_summary_var.trace_add(M,H);P+=1;B.Label(V,text='日语罗马音:').grid(row=P,column=0,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var=C.BooleanVar(value=A.settings[i]);B.Checkbutton(V,text='显示日语假名罗马音',variable=A.show_romaji_for_kana_var).grid(row=P,column=1,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var.trace_add(M,H);P+=1;B.Label(V,text='暗色模式:').grid(row=P,column=0,padx=5,pady=5,sticky=D);A.dark_mode_var=C.StringVar(value=A.settings[S])
		if A.settings[S]==q:A.dark_mode_var.set(AM)
		elif A.settings[S]==A7:A.dark_mode_var.set('开启')
		elif A.settings[S]==A8:A.dark_mode_var.set('关闭')
		A0=[AM,'开启','关闭'];A2=B.Combobox(V,textvariable=A.dark_mode_var,values=A0,state=U);A2.grid(row=P,column=1,padx=5,pady=5,sticky=N);A.dark_mode_var.trace_add(M,H);P+=1;V.grid_columnconfigure(1,weight=1);E=0;B.Label(G,text='全局界面字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.global_font_family_var=C.StringVar(value=A.settings[O]);A3=B.Combobox(G,textvariable=A.global_font_family_var,values=Y,state=U);A3.grid(row=E,column=1,padx=5,pady=5,sticky=N);A.global_font_family_var.trace_add(M,H);E+=1;B.Label(G,text='备用字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.fallback_font_family_var=C.StringVar(value=A.settings[p]);A4=B.Combobox(G,textvariable=A.fallback_font_family_var,values=Y,state=U);A4.grid(row=E,column=1,padx=5,pady=5,sticky=N);A.fallback_font_family_var.trace_add(M,H);E+=1;B.Label(G,text='主单词字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);l=A.settings[Z]
		if l==F or l==A.settings[O]:A.main_word_font_family_var=C.StringVar(value=A1)
		else:A.main_word_font_family_var=C.StringVar(value=l)
		A5=B.Combobox(G,textvariable=A.main_word_font_family_var,values=e,state=U);A5.grid(row=E,column=1,padx=5,pady=5,sticky=N);A.main_word_font_family_var.trace_add(M,H);E+=1;B.Label(G,text='主单词大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.main_word_font_size_var=C.StringVar(value=str(A.settings[f]));A6=B.Spinbox(G,from_=10,to_=72,textvariable=A.main_word_font_size_var,width=5);A6.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.main_word_font_size_var.trace_add(M,H);E+=1;B.Label(G,text='括号文字字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);n=A.settings[a]
		if n==F or n==A.settings[O]:A.bracketed_font_family_var=C.StringVar(value=A1)
		else:A.bracketed_font_family_var=C.StringVar(value=n)
		A9=B.Combobox(G,textvariable=A.bracketed_font_family_var,values=e,state=U);A9.grid(row=E,column=1,padx=5,pady=5,sticky=N);A.bracketed_font_family_var.trace_add(M,H);E+=1;B.Label(G,text='括号文字大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.bracketed_font_size_var=C.StringVar(value=str(A.settings[g]));AA=B.Spinbox(G,from_=8,to_=48,textvariable=A.bracketed_font_size_var,width=5);AA.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.bracketed_font_size_var.trace_add(M,H);E+=1;B.Label(G,text='罗马音字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);r=A.settings[b]
		if r==F or r==A.settings[O]:A.romaji_font_family_var=C.StringVar(value=A1)
		else:A.romaji_font_family_var=C.StringVar(value=r)
		AB=B.Combobox(G,textvariable=A.romaji_font_family_var,values=e,state=U);AB.grid(row=E,column=1,padx=5,pady=5,sticky=N);A.romaji_font_family_var.trace_add(M,H);E+=1;B.Label(G,text='罗马音大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.romaji_font_size_var=C.StringVar(value=str(A.settings[h]));AC=B.Spinbox(G,from_=8,to_=48,textvariable=A.romaji_font_size_var,width=5);AC.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.romaji_font_size_var.trace_add(M,H);E+=1;G.grid_columnconfigure(1,weight=1);Q=0;B.Label(W,text='启用语音朗读:').grid(row=Q,column=0,padx=5,pady=5,sticky=D);A.enable_tts_var=C.BooleanVar(value=A.settings[j]);B.Checkbutton(W,text='开启语音朗读',variable=A.enable_tts_var).grid(row=Q,column=1,padx=5,pady=5,sticky=D);A.enable_tts_var.trace_add(M,H);Q+=1;B.Label(W,text='选择语音:').grid(row=Q,column=0,padx=5,pady=5,sticky=D);AD=[A.name for A in A.tts_voices];A.tts_voice_id_var=C.StringVar()
		if A.settings[J]and any(B.id==A.settings[J]for B in A.tts_voices):
			for t in A.tts_voices:
				if t.id==A.settings[J]:A.tts_voice_id_var.set(t.name);break
		elif A.tts_voices:A.tts_voice_id_var.set(A.tts_voices[0].name)
		AE=B.Combobox(W,textvariable=A.tts_voice_id_var,values=AD,state=U);AE.grid(row=Q,column=1,padx=5,pady=5,sticky=N);A.tts_voice_id_var.trace_add(M,H);Q+=1;B.Label(W,text='音量:').grid(row=Q,column=0,padx=5,pady=5,sticky=D);A.tts_volume_var=C.DoubleVar(value=A.settings[c]);AF=B.Scale(W,from_=.0,to=w,orient=AY,variable=A.tts_volume_var,command=lambda s:H());AF.grid(row=Q,column=1,padx=5,pady=5,sticky=N);Q+=1;B.Label(W,text='语速:').grid(row=Q,column=0,padx=5,pady=5,sticky=D);A.tts_rate_var=C.IntVar(value=A.settings[d]);AG=B.Spinbox(W,from_=50,to_=300,textvariable=A.tts_rate_var,width=5);AG.grid(row=Q,column=1,padx=5,pady=5,sticky=D);A.tts_rate_var.trace_add(M,H);Q+=1;W.grid_columnconfigure(1,weight=1);B.Button(L,text='保存设置',command=lambda:A.save_settings(L)).pack(pady=10);L.protocol(AP,lambda:A.confirm_close_settings(L))
	def confirm_close_settings(A,settings_window):
		B=settings_window
		if A.settings_changed:C=E.askyesnocancel('未保存的更改','您有未保存的设置。是否保存更改？',icon='warning',parent=B)
		else:A.on_settings_close(B)
	def on_settings_close(B,settings_window):A=settings_window;A.grab_release();A.destroy()
	def on_app_close(A):
		if A.tts_engine:
			try:A.tts_engine.stop()
			except Y as B:A3(f"Error stopping TTS engine on app close: {B}")
		A.save_progress();A.master.destroy()
	def save_settings(A,settings_window):
		B=settings_window
		try:
			I={AL:AI,'低调':k,'明显':AJ};A.settings[T]=I[A.reveal_hint_style_var.get()];L={AM:q,'开启':A7,'关闭':A8};A.settings[S]=L[A.dark_mode_var.get()];A.settings[O]=A.global_font_family_var.get();A.settings[p]=A.fallback_font_family_var.get();C=A.main_word_font_family_var.get()
			if C==A1:A.settings[Z]=F
			else:A.settings[Z]=C
			A.settings[f]=int(A.main_word_font_size_var.get());D=A.bracketed_font_family_var.get()
			if D==F:A.settings[a]=F
			else:A.settings[a]=D
			A.settings[g]=int(A.bracketed_font_size_var.get());G=A.romaji_font_family_var.get()
			if G==F:A.settings[b]=F
			else:A.settings[b]=G
			A.settings[h]=int(A.romaji_font_size_var.get());A.settings[j]=A.enable_tts_var.get();M=A.tts_voice_id_var.get()
			for H in A.tts_voices:
				if H.name==M:A.settings[J]=H.id;break
			A.settings[c]=A.tts_volume_var.get();A.settings[d]=A.tts_rate_var.get()
			if A.tts_engine:
				if A.settings[J]:A.tts_engine.setProperty(x,A.settings[J])
				A.tts_engine.setProperty(AQ,A.settings[c]);A.tts_engine.setProperty('rate',A.settings[d])
			A.settings[R]=A.show_session_summary_var.get();A.settings[i]=A.show_romaji_for_kana_var.get();A.save_progress();A.setup_styles();A.settings_changed=K;E.showinfo('设置','设置已保存！',parent=B);A.on_settings_close(B)
		except AB:E.showerror(n,'字体大小、音量或语速必须是有效数字！',parent=B)
		except Y as N:E.showerror(n,f"保存设置时发生错误: {N}",parent=B)
if __name__=='__main__':A=C.Tk();Ag=Af(A);A.mainloop()