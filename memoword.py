AL='settings'
AK='session_start_count'
AJ='direct'
AI='QuizFeedback.TLabel'
AH='QuizQuestion.TLabel'
AG='LearningRomaji.TLabel'
AF='LearningBracketed.TLabel'
AE='LearningSimilar.TLabel'
AD='LearningDefinition.TLabel'
AC='LearningWord.TLabel'
AB=enumerate
AA='跟随系统设置'
A9='不显示'
A8='text'
A7='Obvious'
A6='None'
A5='N/A'
A4='vocabulary_data'
A3='utf-8'
A2='Incorrect.QuizOption.TButton'
A1='Correct.QuizOption.TButton'
A0='Off'
z=str
y=ValueError
x=open
v='无解释'
u='开始学习'
t='black'
s='Arial'
r='Helvetica'
q=Exception
p='bold'
o=range
l='跟随全局字体'
k='15'
j='System'
i='fallback_font_family'
h=list
g='错误'
f='QuizOption.TButton'
e='Subtle'
d='show_romaji_for_kana'
c='romaji_font_size'
b='bracketed_font_size'
a='main_word_font_size'
Z=None
Y='last_study_time'
X='romaji_font_family'
W='bracketed_font_family'
V='main_word_font_family'
T='center'
S='study_count'
R='dark_mode'
Q='reveal_hint_style'
P='ew'
O='i'
N=False
M='show_session_summary'
L='d'
K='o'
J='global_font_family'
I=True
H=len
G=''
F='FollowGlobal'
D='w'
import tkinter as C
from tkinter import ttk as B,filedialog as AM,messagebox as E,font
import json as m
from datetime import datetime as n,timedelta as AN
import os,random as U,re,copy
try:import darkdetect as w
except ImportError:w=Z
class AO:
	def __init__(A,master):z='ppi';y='ppa';x='tto';w='tte';v='ttsu';u='cchi';t='tta';q='sso';p='sse';o='ssu';n='sshi';m='ssa';l='kko';k='kke';h='kku';g='kki';f='kka';Y='mmi';U='zu';T='ji';S='yo';P='yu';L='ya';H='ka';G='u';E='a';D=master;C='e';B='wa';A.master=D;D.title('MemoWord - 记单词');D.geometry('800x600');D.minsize(600,400);A.vocabulary_data=[];A.progress_file='memoword_progress.json';A.session_start_count=0;A.settings={J:r,i:s,V:F,a:36,W:F,b:20,X:F,c:14,Q:e,M:I,d:N,R:j};A.direct_learning_session=[];A.direct_word_index=0;A.quiz_session_words=[];A.quiz_words_to_ask=[];A.incorrectly_answered_words=[];A.current_quiz_word=Z;A.current_quiz_correct_answer=Z;A.quiz_items_completed=0;A.quiz_total_items_to_complete=0;A.recently_learned_for_quiz=[];A.KANA_TO_ROMAJI_MAP={'っか':f,'っき':g,'っく':h,'っけ':k,'っこ':l,'っさ':m,'っし':n,'っす':o,'っせ':p,'っそ':q,'った':t,'っち':u,'っつ':v,'って':w,'っと':x,'っぱ':y,'っぴ':z,'っぷ':'ppu','っぺ':'ppe','っぽ':'ppo','っは':'hha','っひ':'hhi','っふ':'ffu','っへ':'hhe','っほ':'hho','っま':'mma','っみ':Y,'っむ':'mmu','っめ':'mme','っも':'mmo','っや':'yya','っゆ':'yyu','っよ':'yyo','っら':'rra','っり':'rri','っる':'rru','っれ':'rre','っろ':'rro','っわ':'wwa','ッか':f,'ッキ':g,'ック':h,'ッケ':k,'ッコ':l,'ッサ':m,'ッシ':n,'ッス':o,'ッセ':p,'ッソ':q,'ッタ':t,'ッチ':u,'ッツ':v,'ッテ':w,'ット':x,'ッパ':y,'ッピ':z,'ップ':'ppu','ッペ':'ppe','ッポ':'ppo','ッハ':'hha','ッヒ':'hhi','ッフ':'ffu','ッヘ':'hhe','ッホ':'hho','ッマ':'mma','ッミ':Y,'ッム':'mmu','ッメ':'mme','ッモ':'mmo','ッヤ':'yya','ッユ':'yyu','ッヨ':'yyo','ッラ':'rra','ッリ':'rri','ッル':'rru','ッレ':'rre','ッロ':'rro','ッワ':'wwa','きゃ':'kya','きゅ':'kyu','きょ':'kyo','しゃ':'sha','しゅ':'shu','しょ':'sho','ちゃ':'cha','ちゅ':'chu','ちょ':'cho','にゃ':'nya','にゅ':'nyu','にょ':'nyo','ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','みゃ':'mya','みゅ':'myu','みょ':'myo','りゃ':'rya','りゅ':'ryu','りょ':'ryo','ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo','じゃ':'ja','じゅ':'ju','じょ':'jo','びゃ':'bya','びゅ':'byu','びょ':'byo','ぴゃ':'pya','ぴゅ':'pyu','ぴょ':'pyo','キャ':'kya','キュ':'kyu','キョ':'kyo','シャ':'sha','シュ':'shu','ショ':'sho','チャ':'cha','チュ':'chu','チョ':'cho','ニャ':'nya','ニュ':'nyu','ニョ':'nyo','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','ミャ':'mya','ミュ':'myu','ミョ':'myo','リャ':'rya','リュ':'ryu','リョ':'ryo','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ジャ':'ja','ジュ':'ju','ジョ':'jo','ビャ':'bya','ビュ':'byu','ビョ':'byo','ピャ':'pya','ピュ':'pyu','ピョ':'pyo','ああ':'aa','いい':'ii','うう':'uu','ええ':'ee','おお':'oo','おう':'oo','ー':'-','は':B,'へ':C,'を':K,'あ':E,'い':O,'う':G,'え':C,'お':K,'か':H,'き':'ki','く':'ku','け':'ke','こ':'ko','さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to','な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':L,'ゆ':P,'よ':S,'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','わ':B,'ゐ':'wi','ゑ':'we','を':'wo','ん':'n','が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ざ':'za','じ':T,'ず':U,'ぜ':'ze','ぞ':'zo','だ':'da','ぢ':T,'づ':U,'で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ア':E,'イ':O,'ウ':G,'エ':C,'オ':K,'カ':H,'キ':'ki','ク':'ku','ケ':'ke','コ':'ko','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','マ':'ma','ミ':Y,'ム':'mu','メ':'me','モ':'mo','ヤ':L,'ユ':P,'ヨ':S,'ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro','ワ':B,'ヰ':'wi','ヱ':'we','ヲ':'wo','ン':'n','ガ':'ga','ギ':'gi','グ':'gu','ゲ':'ge','ゴ':'go','ザ':'za','ジ':T,'ズ':U,'ゼ':'ze','ゾ':'zo','ダ':'da','ヂ':T,'ヅ':U,'デ':'de','ド':'do','バ':'ba','ビ':'bi','ブ':'bu','ベ':'be','ボ':'bo','パ':'pa','ピ':'pi','プ':'pu','ペ':'pe','ポ':'po','ぁ':E,'ぃ':O,'ぅ':G,'ぇ':C,'ぉ':K,'ァ':E,'ィ':O,'ゥ':G,'ェ':C,'ォ':K,'ゃ':L,'ゅ':P,'ょ':S,'ャ':L,'ュ':P,'ョ':S,'ゎ':B,'ヮ':B,'ヶ':H,'ヵ':H};A.setup_styles();A.create_widgets();A.load_initial_data()
	def setup_styles(G):
		A9='Treeview';A8='TButton';A7='#87ceeb';A6='#555555';A5='#0056b3';A4='#ffffff';A3='bg_checkbutton';z='fg_hint_obvious';y='fg_hint_subtle';s='#2b2b2b';r='#f0f0f0';q='bg_selected_treeview';o='fg_romaji';n='fg_incorrect_button';m='fg_correct_button';l='fg_quiz_question';k='fg_learning_word';j='fg_treeview_heading';i='bg_treeview_heading';h='fg_treeview';g='bg_treeview';Y='#333333';U='fg_active_button';T='bg_active_button';S='fg_similar_words';Q='bg_frame';P='bg_incorrect_button';O='bg_correct_button';N='fg_label';M='!disabled';L='active';K='#e0e0e0';I='fg_button';H='bg_button';E='bg_label';C=B.Style();C.theme_use('clam');u={Q:r,E:r,N:Y,H:'#dddddd',I:Y,g:A4,h:Y,i:K,j:Y,k:A5,l:A5,O:'lightgreen',m:t,P:'salmon',n:t,y:'gray',z:'blue',S:'#666666',o:'#888888',A3:r,T:K,U:'#000000',q:'#a8d8ff'};v={Q:s,E:s,N:K,H:'#444444',I:K,g:'#3c3c3c',h:K,i:A6,j:K,k:A7,l:A7,O:'#4CAF50',m:'white',P:'#FF6347',n:'white',y:'#aaaaaa',z:'#add8e6',S:'#bbbbbb',o:'#cccccc',A3:s,T:A6,U:A4,q:'#5a5a5a'};x=G.settings[R]
		if x=='On':A=v
		elif x==A0:A=u
		elif w and w.isDark():A=v
		else:A=u
		D=G.settings[J];Z=G.settings[V]
		if Z==F:Z=D
		d=G.settings[W]
		if d==F:d=D
		e=G.settings[X]
		if e==F:e=D
		C.configure('TFrame',background=A[Q]);C.configure('TLabel',background=A[E],foreground=A[N],font=(D,10));C.configure(A8,font=(D,10),padding=6,background=A[H],foreground=A[I]);C.map(A8,background=[(L,A[T]),(M,A[H])],foreground=[(L,A[U]),(M,A[I])]);C.configure('Treeview.Heading',font=(D,10,p),background=A[i],foreground=A[j]);C.configure(A9,font=(D,10),rowheight=25,background=A[g],foreground=A[h]);C.map(A9,background=[('selected',A[q])]);C.configure(AC,font=(Z,G.settings[a],p),foreground=A[k],background=A[E]);C.configure(AD,font=(D,18),foreground=A[N],background=A[E]);C.configure(AE,font=(D,12),foreground=A[S],background=A[E]);C.configure(AF,font=(d,G.settings[b]),foreground=A[S],background=A[E]);C.configure(AG,font=(e,G.settings[c]),foreground=A[o],background=A[E]);C.configure(AH,font=(D,20,p),foreground=A[l],background=A[E],wraplength=700);C.configure(f,font=(D,14),padding=10,background=A[H],foreground=A[I]);C.map(f,background=[(L,A[T]),(M,A[H])],foreground=[(L,A[U]),(M,A[I])]);C.configure(AI,font=(D,14,p),background=A[E]);C.configure(A1,background=A[O],foreground=A[m]);C.map(A1,background=[(L,A[O]),(M,A[O])]);C.configure(A2,background=A[P],foreground=A[n]);C.map(A2,background=[(L,A[P]),(M,A[P])]);C.configure('TCheckbutton',background=A[E],foreground=A[N],font=(D,10));C.configure('TCombobox',font=(D,10));C.configure('TSpinbox',font=(D,10));G.master.config(bg=A[Q])
	def create_widgets(A):A.main_frame=B.Frame(A.master,padding=k);A.main_frame.pack(fill=C.BOTH,expand=I);A.learning_frame=B.Frame(A.master,padding=k);A.progress_bar=B.Progressbar(A.learning_frame,orient='horizontal',mode='determinate');A.progress_bar.pack(fill=C.X,pady=5);A.create_main_page_widgets();A.create_direct_learning_widgets();A.create_quiz_widgets()
	def create_main_page_widgets(A):G='definition';F='word';B.Label(A.main_frame,text='MemoWord 词汇表',font=(A.settings[J],18,p)).pack(pady=15);A.total_study_label=B.Label(A.main_frame,text='进入学习界面次数: 0',font=(A.settings[J],12));A.total_study_label.pack(pady=5);A.vocab_tree=B.Treeview(A.main_frame,columns=(F,G,S,Y),show='headings');A.vocab_tree.heading(F,text='词汇');A.vocab_tree.heading(G,text='解释');A.vocab_tree.heading(S,text='学习次数');A.vocab_tree.heading(Y,text='上次学习时间');A.vocab_tree.column(F,width=150,minwidth=100,anchor=T);A.vocab_tree.column(G,width=300,minwidth=200,anchor=D);A.vocab_tree.column(S,width=100,minwidth=80,anchor=T);A.vocab_tree.column(Y,width=150,minwidth=120,anchor=T);A.vocab_tree.pack(fill=C.BOTH,expand=I,pady=10);H=B.Scrollbar(A.vocab_tree,orient='vertical',command=A.vocab_tree.yview);H.pack(side='right',fill='y');A.vocab_tree.configure(yscrollcommand=H.set);E=B.Frame(A.main_frame);E.pack(pady=15);A.import_button=B.Button(E,text='导入词汇表',command=A.load_vocabulary);A.import_button.pack(side=C.LEFT,padx=10);A.start_learning_button=B.Button(E,text=u,command=A.start_learning);A.start_learning_button.pack(side=C.LEFT,padx=10);A.settings_button=B.Button(E,text='设置',command=A.open_settings);A.settings_button.pack(side=C.LEFT,padx=10)
	def create_direct_learning_widgets(A):A.direct_learning_sub_frame=B.Frame(A.learning_frame,padding=k);A.learning_romaji_label=B.Label(A.direct_learning_sub_frame,text=G,style=AG,wraplength=700,anchor=T);A.learning_romaji_label.pack(pady=(20,0),fill=C.X);A.learning_word_label=B.Label(A.direct_learning_sub_frame,text=G,style=AC,wraplength=700,anchor=T);A.learning_word_label.pack(pady=(5,0),fill=C.X);A.learning_bracketed_label=B.Label(A.direct_learning_sub_frame,text=G,style=AF,wraplength=700,anchor=T);A.learning_bracketed_label.pack(pady=(5,20),fill=C.X);A.learning_definition_label=B.Label(A.direct_learning_sub_frame,text=G,style=AD,wraplength=700,anchor=T);A.learning_definition_label.pack(pady=20,fill=C.X);A.learning_similar_label=B.Label(A.direct_learning_sub_frame,text=G,style=AE,wraplength=700,anchor=T);A.learning_similar_label.pack(pady=10,fill=C.X);D=B.Frame(A.direct_learning_sub_frame);D.pack(pady=30);A.reveal_button=B.Button(D,text='显示解释',command=A.reveal_definition);A.reveal_button.pack(side=C.LEFT,padx=15);A.next_word_button=B.Button(D,text='下一个',command=A.next_direct_word,state=C.DISABLED);A.next_word_button.pack(side=C.LEFT,padx=15);A.back_to_main_button_direct=B.Button(A.direct_learning_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_direct.pack(pady=20)
	def create_quiz_widgets(A):
		A.quiz_sub_frame=B.Frame(A.learning_frame,padding=k);A.quiz_question_label=B.Label(A.quiz_sub_frame,text=G,style=AH,anchor=T);A.quiz_question_label.pack(pady=40,fill=C.X);A.quiz_options_frame=B.Frame(A.quiz_sub_frame);A.quiz_options_frame.pack(pady=20,fill=C.X,expand=I);A.quiz_options_frame.grid_columnconfigure(0,weight=1);A.quiz_options_frame.grid_columnconfigure(1,weight=1);A.quiz_option_buttons=[]
		for D in o(4):E=B.Button(A.quiz_options_frame,text=f"Option {D+1}",style=f);E.grid(row=D//2,column=D%2,padx=10,pady=10,sticky=P);A.quiz_option_buttons.append(E);E.grid_forget()
		A.quiz_feedback_label=B.Label(A.quiz_sub_frame,text=G,style=AI);A.quiz_feedback_label.pack(pady=15);A.quiz_next_button=B.Button(A.quiz_sub_frame,text='下一个问题',command=A.next_quiz_question,state=C.DISABLED);A.quiz_next_button.pack(pady=10);A.back_to_main_button_quiz=B.Button(A.quiz_sub_frame,text='返回主页',command=A.show_main_page);A.back_to_main_button_quiz.pack(pady=20)
	def show_main_page(A):A.learning_frame.pack_forget();A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack_forget();A.main_frame.pack(fill=C.BOTH,expand=I);A.update_main_page_display()
	def show_learning_page(A,mode):
		A.main_frame.pack_forget();A.learning_frame.pack(fill=C.BOTH,expand=I);A.progress_bar.config(value=0)
		if mode==AJ:A.quiz_sub_frame.pack_forget();A.direct_learning_sub_frame.pack(fill=C.BOTH,expand=I)
		elif mode=='quiz':A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack(fill=C.BOTH,expand=I)
	def load_initial_data(A):A.load_progress();A.update_main_page_display()
	def load_vocabulary(C):
		N=AM.askopenfilename(filetypes=[('JSON files','*.json')])
		if not N:return
		try:
			with x(N,'r',encoding=A3)as U:P=m.load(U)
			J={A[D]:A for A in C.vocabulary_data};M=[]
			for A in P:
				F=A.get(D)
				if not F:continue
				if F in J:B=J[F];B[L]=A.get(L,B.get(L,G));B[K]=A.get(K,B.get(K,[]));B[O]=A.get(O,B.get(O,0));M.append(B)
				else:M.append({O:A.get(O,0),D:F,L:A.get(L,G),K:A.get(K,[]),S:0,Y:Z})
			I={}
			for Q in M:I[Q[D]]=Q
			for(R,V)in J.items():
				if R not in I:I[R]=V
			C.vocabulary_data=h(I.values());C.vocabulary_data.sort(key=lambda x:x.get(O,0));C.save_progress();C.update_main_page_display();E.showinfo('导入成功',f"成功导入 {H(P)} 个词汇。")
		except m.JSONDecodeError:E.showerror(g,'无效的JSON文件格式。请确保文件内容符合JSON规范。')
		except q as T:E.showerror(g,f"导入词汇时发生错误: {T}");print(f"Error during import: {T}")
		finally:C.master.focus_set()
	def load_progress(A):
		if os.path.exists(A.progress_file):
			try:
				with x(A.progress_file,'r',encoding=A3)as C:
					B=m.load(C)
					if isinstance(B,dict)and A4 in B:A.vocabulary_data=B.get(A4,[]);A.session_start_count=B.get(AK,0);A.settings.update(B.get(AL,{}))
					else:A.vocabulary_data=B;A.session_start_count=0
			except m.JSONDecodeError:E.showerror(g,'学习进度文件损坏或格式不正确，将重新创建。',parent=A.master);A.vocabulary_data=[];A.session_start_count=0;A.settings={J:r,i:s,V:F,a:36,W:F,b:20,X:F,c:14,Q:e,M:I,d:N,R:j}
			except q as D:E.showerror(g,f"加载学习进度时发生错误: {D}",parent=A.master);A.vocabulary_data=[];A.session_start_count=0;A.settings={J:r,i:s,V:F,a:36,W:F,b:20,X:F,c:14,Q:e,M:I,d:N,R:j}
		else:A.vocabulary_data=[];A.session_start_count=0;A.settings={J:r,i:s,V:F,a:36,W:F,b:20,X:F,c:14,Q:e,M:I,d:N,R:j}
	def save_progress(A):
		try:
			B={A4:A.vocabulary_data,AK:A.session_start_count,AL:A.settings}
			with x(A.progress_file,D,encoding=A3)as C:m.dump(B,C,ensure_ascii=N,indent=4)
		except q as F:E.showerror(g,f"保存学习进度时发生错误: {F}",parent=A.master)
	def update_main_page_display(A):
		for H in A.vocab_tree.get_children():A.vocab_tree.delete(H)
		for B in A.vocabulary_data:
			I=B.get(D,A5);J=B.get(L,A5);K=B.get(S,0);F=B.get(Y);E='未学习'
			if F:
				try:M=n.fromisoformat(F);E=M.strftime('%Y-%m-%d %H:%M')
				except y:E='日期格式错误'
			A.vocab_tree.insert(G,C.END,values=(I,J,K,E))
		A.total_study_label.config(text=f"进入学习界面次数: {A.session_start_count}")
	def start_learning(A):
		if not A.vocabulary_data:E.showwarning('提示','请先导入词汇表！',parent=A.master);return
		A.session_start_count+=1;A.save_progress();D=[];C=[];F=[];J=n.now();K=J-AN(days=3)
		for B in A.vocabulary_data:
			G=B.get(S,0);I=B.get(Y)
			if G==0:D.append(B)
			elif I:
				try:
					L=n.fromisoformat(I)
					if G<15 and L<K:C.append(B)
					else:F.append(B)
				except y:C.append(B)
			else:C.append(B)
		D.sort(key=lambda x:x.get(O,0))
		if C:
			if A.settings[M]:E.showinfo(u,f"有 {H(C)} 个单词需要优先复习！",parent=A.master)
			A.start_quiz_session(C)
		elif A.recently_learned_for_quiz:
			if A.settings[M]:E.showinfo('开始复习',f"开始复习刚刚学习的 {H(A.recently_learned_for_quiz)} 个单词！",parent=A.master)
			N=h(A.recently_learned_for_quiz);A.recently_learned_for_quiz.clear();A.start_quiz_session(N)
		elif D:
			A.direct_learning_session=D[:5]
			if A.settings[M]:E.showinfo(u,f"开始学习 {H(A.direct_learning_session)} 个新单词！",parent=A.master)
			A.start_direct_learning_session()
		else:
			if not F:E.showinfo('恭喜','所有单词都已学习或复习完毕！',parent=A.master);return
			U.shuffle(F);A.quiz_session_words=F[:10]
			if A.settings[M]:E.showinfo(u,f"开始复习 {H(A.quiz_session_words)} 个旧单词！",parent=A.master)
			A.start_quiz_session(A.quiz_session_words)
		A.master.focus_set()
	def start_direct_learning_session(A):
		A.direct_word_index=0
		if A.direct_learning_session:A.show_learning_page(AJ);A.progress_bar.config(maximum=H(A.direct_learning_session),value=0);A.display_current_direct_word()
		else:A.show_main_page()
	def _kana_to_romaji(E,kana_text):
		B=kana_text;C=[];A=0
		while A<H(B):
			K=N
			for J in o(3,0,-1):
				if A+J<=H(B):
					D=B[A:A+J]
					if D in E.KANA_TO_ROMAJI_MAP:
						if D=='ー'and C:
							L=re.search('[aeiou]$',C[-1])
							if L:C[-1]+=L.group(0)
							else:C.append('-')
						elif D in['ん','ン']and A+1<H(B)and re.match('[あいうえおやゆよアイウエオヤユヨ]',B[A+1]):C.append("n'")
						elif D in['っ','ッ']and A+1<H(B):
							F=Z
							for M in o(3,0,-1):
								if A+1+M<=H(B):
									O=B[A+1:A+1+M]
									if O in E.KANA_TO_ROMAJI_MAP:F=E.KANA_TO_ROMAJI_MAP[O];break
							if F and F[0].isalpha():C.append(F[0])
						else:C.append(E.KANA_TO_ROMAJI_MAP[D])
						A+=J;K=I;break
			if not K:C.append(B[A]);A+=1
		return G.join(C)
	def display_current_direct_word(A):
		P="点击 '显示解释' 查看";O='〔.*?〕'
		if A.direct_word_index<H(A.direct_learning_session):
			I=A.direct_learning_session[A.direct_word_index];B=I.get(D,G);A.progress_bar.config(value=A.direct_word_index+1)
			if A.settings[d]:R=re.sub(O,G,B);S=G.join(A for A in R if'\u3040'<=A<='ゟ'or'゠'<=A<='ヿ'or A=='ー');T=A._kana_to_romaji(S);A.learning_romaji_label.config(text=T)
			else:A.learning_romaji_label.config(text=G)
			J=re.search(O,B)
			if J:L=J.group(0);U=B.replace(L,G).strip();A.learning_word_label.config(text=U);A.learning_bracketed_label.config(text=L)
			else:A.learning_word_label.config(text=B);A.learning_bracketed_label.config(text=G)
			F=A.settings[Q]
			if F==A6:A.learning_definition_label.config(text=G,foreground=t)
			elif F==e:A.learning_definition_label.config(text=P,foreground='gray')
			elif F==A7:A.learning_definition_label.config(text=P,foreground='blue')
			N=', '.join(I.get(K,[]));A.learning_similar_label.config(text=f"形近/音近词: {N}"if N else'无形近/音近词');A.reveal_button.config(state=C.NORMAL);A.next_word_button.config(state=C.DISABLED)
		elif A.direct_learning_session:
			A.recently_learned_for_quiz=h(A.direct_learning_session)
			if A.settings[M]:E.showinfo('学习完成',f"本次新词学习已完成！接下来将复习刚刚学习的 {H(A.recently_learned_for_quiz)} 个单词。",parent=A.master)
			A.start_quiz_session(A.recently_learned_for_quiz)
		else:E.showinfo('学习结束','本次学习已完成！',parent=A.master);A.show_main_page()
	def reveal_definition(A):
		if A.direct_word_index<H(A.direct_learning_session):
			B=A.direct_learning_session[A.direct_word_index];A.learning_definition_label.config(text=B.get(L,v),foreground=t);A.reveal_button.config(state=C.DISABLED);A.next_word_button.config(state=C.NORMAL);G=B.get(D)
			for(E,F)in AB(A.vocabulary_data):
				if F.get(D)==G:A.vocabulary_data[E][S]=F.get(S,0)+1;A.vocabulary_data[E][Y]=n.now().isoformat();break
			A.save_progress()
	def next_direct_word(A):A.direct_word_index+=1;A.display_current_direct_word()
	def start_quiz_session(A,words_to_quiz_initial=Z):
		C=words_to_quiz_initial;A.incorrectly_answered_words=[];A.quiz_items_completed=0;A.quiz_words_to_ask=[];B=[]
		if C is not Z:B=h(C)
		else:B=h(A.quiz_session_words)
		for D in B:
			for F in o(3):A.quiz_words_to_ask.append(D)
		U.shuffle(A.quiz_words_to_ask);A.quiz_total_items_to_complete=H(A.quiz_words_to_ask)
		if A.quiz_words_to_ask:A.show_learning_page('quiz');A.progress_bar.config(maximum=A.quiz_total_items_to_complete,value=A.quiz_items_completed);A.display_quiz_question()
		else:E.showinfo('测验结束','本次测验已完成！',parent=A.master);A.show_main_page()
	def display_quiz_question(A):
		d='multiple_choice';T='False';S='True';A.quiz_feedback_label.config(text=G)
		for M in A.quiz_option_buttons:M.destroy()
		A.quiz_option_buttons=[];A.quiz_next_button.config(state=C.DISABLED)
		if A.incorrectly_answered_words:A.current_quiz_word=A.incorrectly_answered_words.pop(0)
		elif A.quiz_words_to_ask:A.current_quiz_word=A.quiz_words_to_ask.pop(0)
		else:E.showinfo('测验结束','恭喜！所有题目都已答对！',parent=A.master);A.show_main_page();return
		e=U.choice([d,'true_false']);F=[];J=G
		if e==d:
			Q=f"请选择与 '{A.current_quiz_word.get(L,v)}' 对应的单词：";J=A.current_quiz_word.get(D);F.append(J);V=[A for A in A.current_quiz_word.get(K,[])if A!=J];U.shuffle(V);W=[A[D]for A in A.vocabulary_data if A[D]!=J];U.shuffle(W)
			for X in V:
				if H(F)<4 and X not in F:F.append(X)
			for Y in W:
				if H(F)<4 and Y not in F:F.append(Y)
			while H(F)<4:F.append(f"选项 {H(F)+1}")
			U.shuffle(F);A.current_quiz_correct_answer=J;A.quiz_question_label.config(text=Q)
			for O in o(4):M=B.Button(A.quiz_options_frame,text=F[O],style=f,command=lambda i=O:A.check_quiz_answer(A.quiz_option_buttons[i][A8]));M.grid(row=O//2,column=O%2,padx=10,pady=10,sticky=P);A.quiz_option_buttons.append(M)
		else:
			g=A.current_quiz_word.get(D,A5);Z=A.current_quiz_word.get(L,v);h=U.choice([I,N])
			if h:R=Z;A.current_quiz_correct_answer=S
			else:
				a=[A[L]for A in A.vocabulary_data if A[L]!=Z and A[L]!=v]
				if a:R=U.choice(a)
				else:R='一个不正确的解释'
				A.current_quiz_correct_answer=T
			Q=f"'{g}' 的意思是 '{R}'，这个说法对吗？";A.quiz_question_label.config(text=Q);b=B.Button(A.quiz_options_frame,text=S,style=f,command=lambda:A.check_quiz_answer(S));b.grid(row=0,column=0,padx=10,pady=10,sticky=P);A.quiz_option_buttons.append(b);c=B.Button(A.quiz_options_frame,text=T,style=f,command=lambda:A.check_quiz_answer(T));c.grid(row=0,column=1,padx=10,pady=10,sticky=P);A.quiz_option_buttons.append(c)
	def check_quiz_answer(A,selected_answer):
		E=selected_answer;F=E==A.current_quiz_correct_answer
		if F:A.quiz_feedback_label.config(text='正确！',foreground='green');A.quiz_items_completed+=1
		else:
			A.quiz_feedback_label.config(text=f"错误！正确答案是: {A.current_quiz_correct_answer}",foreground='red')
			if A.current_quiz_word not in A.incorrectly_answered_words:A.incorrectly_answered_words.append(A.current_quiz_word)
		I=A.current_quiz_word.get(D)
		for(G,H)in AB(A.vocabulary_data):
			if H.get(D)==I:A.vocabulary_data[G][S]=H.get(S,0)+1;A.vocabulary_data[G][Y]=n.now().isoformat();break
		A.save_progress();A.progress_bar.config(value=A.quiz_items_completed)
		for B in A.quiz_option_buttons:
			B.config(state=C.DISABLED)
			if B[A8]==A.current_quiz_correct_answer:B.config(style=A1)
			elif B[A8]==E and not F:B.config(style=A2)
			else:B.config(style=f)
		A.quiz_next_button.config(state=C.NORMAL)
	def next_quiz_question(A):A.display_quiz_question()
	def open_settings(A):
		T='readonly';L='write';O=C.Toplevel(A.master);O.title('设置');O.geometry('500x450');O.resizable(N,N);O.transient(A.master);O.grab_set();O.focus_set();A.original_settings=copy.deepcopy(A.settings);A.settings_changed=N
		def H(*B):A.settings_changed=I
		U=B.Notebook(O);U.pack(pady=10,padx=10,fill=C.BOTH,expand=I);S=B.Frame(U,padding=k);U.add(S,text='显示设置');G=B.Frame(U,padding=k);U.add(G,text='字体设置');Y=sorted(h(font.families()));Z=[l]+Y;K=0;B.Label(S,text='解释提示样式:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.reveal_hint_style_var=C.StringVar(value=A.settings[Q])
		if A.settings[Q]==A6:A.reveal_hint_style_var.set(A9)
		elif A.settings[Q]==e:A.reveal_hint_style_var.set('低调')
		elif A.settings[Q]==A7:A.reveal_hint_style_var.set('明显')
		n=[A9,'低调','明显'];o=B.Combobox(S,textvariable=A.reveal_hint_style_var,values=n,state=T);o.grid(row=K,column=1,padx=5,pady=5,sticky=P);A.reveal_hint_style_var.trace_add(L,H);K+=1;B.Label(S,text='学习概述:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.show_session_summary_var=C.BooleanVar(value=A.settings[M]);B.Checkbutton(S,text='显示学习内容概述',variable=A.show_session_summary_var).grid(row=K,column=1,padx=5,pady=5,sticky=D);A.show_session_summary_var.trace_add(L,H);K+=1;B.Label(S,text='日语罗马音:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var=C.BooleanVar(value=A.settings[d]);B.Checkbutton(S,text='显示日语假名罗马音',variable=A.show_romaji_for_kana_var).grid(row=K,column=1,padx=5,pady=5,sticky=D);A.show_romaji_for_kana_var.trace_add(L,H);K+=1;B.Label(S,text='暗色模式:').grid(row=K,column=0,padx=5,pady=5,sticky=D);A.dark_mode_var=C.StringVar(value=A.settings[R])
		if A.settings[R]==j:A.dark_mode_var.set(AA)
		elif A.settings[R]=='On':A.dark_mode_var.set('开启')
		elif A.settings[R]==A0:A.dark_mode_var.set('关闭')
		p=[AA,'开启','关闭'];q=B.Combobox(S,textvariable=A.dark_mode_var,values=p,state=T);q.grid(row=K,column=1,padx=5,pady=5,sticky=P);A.dark_mode_var.trace_add(L,H);K+=1;S.grid_columnconfigure(1,weight=1);E=0;B.Label(G,text='全局界面字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.global_font_family_var=C.StringVar(value=A.settings[J]);r=B.Combobox(G,textvariable=A.global_font_family_var,values=Y,state=T);r.grid(row=E,column=1,padx=5,pady=5,sticky=P);A.global_font_family_var.trace_add(L,H);E+=1;B.Label(G,text='备用字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.fallback_font_family_var=C.StringVar(value=A.settings[i]);s=B.Combobox(G,textvariable=A.fallback_font_family_var,values=Y,state=T);s.grid(row=E,column=1,padx=5,pady=5,sticky=P);A.fallback_font_family_var.trace_add(L,H);E+=1;B.Label(G,text='主单词字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);f=A.settings[V]
		if f==F or f==A.settings[J]:A.main_word_font_family_var=C.StringVar(value=l)
		else:A.main_word_font_family_var=C.StringVar(value=f)
		t=B.Combobox(G,textvariable=A.main_word_font_family_var,values=Z,state=T);t.grid(row=E,column=1,padx=5,pady=5,sticky=P);A.main_word_font_family_var.trace_add(L,H);E+=1;B.Label(G,text='主单词大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.main_word_font_size_var=C.StringVar(value=z(A.settings[a]));u=B.Spinbox(G,from_=10,to_=72,textvariable=A.main_word_font_size_var,width=5);u.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.main_word_font_size_var.trace_add(L,H);E+=1;B.Label(G,text='括号文字字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);g=A.settings[W]
		if g==F or g==A.settings[J]:A.bracketed_font_family_var=C.StringVar(value=l)
		else:A.bracketed_font_family_var=C.StringVar(value=g)
		v=B.Combobox(G,textvariable=A.bracketed_font_family_var,values=Z,state=T);v.grid(row=E,column=1,padx=5,pady=5,sticky=P);A.bracketed_font_family_var.trace_add(L,H);E+=1;B.Label(G,text='括号文字大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.bracketed_font_size_var=C.StringVar(value=z(A.settings[b]));w=B.Spinbox(G,from_=8,to_=48,textvariable=A.bracketed_font_size_var,width=5);w.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.bracketed_font_size_var.trace_add(L,H);E+=1;B.Label(G,text='罗马音字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);m=A.settings[X]
		if m==F or m==A.settings[J]:A.romaji_font_family_var=C.StringVar(value=l)
		else:A.romaji_font_family_var=C.StringVar(value=m)
		x=B.Combobox(G,textvariable=A.romaji_font_family_var,values=Z,state=T);x.grid(row=E,column=1,padx=5,pady=5,sticky=P);A.romaji_font_family_var.trace_add(L,H);E+=1;B.Label(G,text='罗马音大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);A.romaji_font_size_var=C.StringVar(value=z(A.settings[c]));y=B.Spinbox(G,from_=8,to_=48,textvariable=A.romaji_font_size_var,width=5);y.grid(row=E,column=1,padx=5,pady=5,sticky=D);A.romaji_font_size_var.trace_add(L,H);E+=1;G.grid_columnconfigure(1,weight=1);B.Button(O,text='保存设置',command=lambda:A.save_settings(O)).pack(pady=10);O.protocol('WM_DELETE_WINDOW',lambda:A.confirm_close_settings(O))
	def confirm_close_settings(A,settings_window):
		B=settings_window
		if A.settings_changed:C=E.askyesnocancel('未保存的更改','您有未保存的设置。是否保存更改？',icon='warning',parent=B)
		else:A.on_settings_close(B)
	def on_settings_close(B,settings_window):A=settings_window;A.grab_release();A.destroy()
	def save_settings(A,settings_window):
		B=settings_window
		try:
			H={A9:A6,'低调':e,'明显':A7};A.settings[Q]=H[A.reveal_hint_style_var.get()];I={AA:j,'开启':'On','关闭':A0};A.settings[R]=I[A.dark_mode_var.get()];A.settings[J]=A.global_font_family_var.get();A.settings[i]=A.fallback_font_family_var.get();C=A.main_word_font_family_var.get()
			if C==l:A.settings[V]=F
			else:A.settings[V]=C
			A.settings[a]=int(A.main_word_font_size_var.get());D=A.bracketed_font_family_var.get()
			if D==F:A.settings[W]=F
			else:A.settings[W]=D
			A.settings[b]=int(A.bracketed_font_size_var.get());G=A.romaji_font_family_var.get()
			if G==l:A.settings[X]=F
			else:A.settings[X]=G
			A.settings[c]=int(A.romaji_font_size_var.get());A.settings[M]=A.show_session_summary_var.get();A.settings[d]=A.show_romaji_for_kana_var.get();A.save_progress();A.setup_styles();A.settings_changed=N;E.showinfo('设置','设置已保存！',parent=B);A.on_settings_close(B)
		except y:E.showerror(g,'字体大小必须是整数！',parent=B)
		except q as K:E.showerror(g,f"保存设置时发生错误: {K}",parent=B)
if __name__=='__main__':A=C.Tk();AP=AO(A);A.mainloop()