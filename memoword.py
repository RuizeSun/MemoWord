AH='settings'
AG='session_start_count'
AF='direct'
AE='QuizFeedback.TLabel'
AD='QuizQuestion.TLabel'
AC='LearningRomaji.TLabel'
AB='LearningBracketed.TLabel'
AA='LearningSimilar.TLabel'
A9='LearningDefinition.TLabel'
A8='LearningWord.TLabel'
A6='不显示'
A5='Obvious'
A4='None'
A3='N/A'
A2='vocabulary_data'
A1='utf-8'
A0='text'
z='Incorrect.QuizOption.TButton'
y='Correct.QuizOption.TButton'
x='ー'
w=int
v=str
u=enumerate
t=ValueError
s=open
r=range
q='开始学习'
p='black'
o='Arial'
n='Helvetica'
m=Exception
l='QuizOption.TButton'
k='bold'
h='15'
g=None
f='fallback_font_family'
e=list
d='跟随全局字体'
c='错误'
b='ew'
a='Subtle'
Z='show_romaji_for_kana'
Y='romaji_font_size'
X='bracketed_font_size'
W='main_word_font_size'
U='last_study_time'
T=False
S='romaji_font_family'
R='bracketed_font_family'
Q='main_word_font_family'
P='center'
O='study_count'
N='d'
M='i'
L='show_session_summary'
K='o'
J='reveal_hint_style'
I='global_font_family'
H=True
G=''
F='FollowGlobal'
B=len
D='w'
import tkinter as C
from tkinter import ttk as A,filedialog as AI,messagebox as E,font
import json as i
from datetime import datetime as j,timedelta as AJ
import os,random as V,re
class AK:
	def __init__(A,master):z='ppu';y='ppi';w='ppa';v='tto';u='tte';t='ttsu';s='cchi';r='tta';q='sso';p='sse';m='ssu';l='sshi';k='ssa';j='kko';i='kke';h='kku';e='kki';d='kka';c='mmi';b='zu';V='ji';U='yo';P='yu';O='ya';N='ka';G='u';E='a';D=master;C='e';B='wa';A.master=D;D.title('MemoWord - 记单词');D.geometry('800x600');D.minsize(600,400);A.vocabulary_data=[];A.progress_file='memoword_progress.json';A.session_start_count=0;A.settings={I:n,f:o,Q:F,W:36,R:F,X:20,S:F,Y:14,J:a,L:H,Z:T};A.direct_learning_session=[];A.direct_word_index=0;A.quiz_session_words=[];A.quiz_words_to_ask=[];A.incorrectly_answered_words=[];A.current_quiz_word=g;A.current_quiz_correct_answer=g;A.quiz_items_completed=0;A.quiz_total_items_to_complete=0;A.recently_learned_for_quiz=[];A.KANA_TO_ROMAJI_MAP={'っか':d,'っき':e,'っく':h,'っけ':i,'っこ':j,'っさ':k,'っし':l,'っす':m,'っせ':p,'っそ':q,'った':r,'っち':s,'っつ':t,'って':u,'っと':v,'っぱ':w,'っぴ':y,'っぷ':z,'っぺ':'ppe','っぽ':'ppo','っは':'hha','っひ':'hhi','っふ':'ffu','っへ':'hhe','っほ':'hho','っま':'mma','っみ':c,'っむ':'mmu','っめ':'mme','っも':'mmo','っや':'yya','っゆ':'yyu','っよ':'yyo','っら':'rra','っり':'rri','っる':'rru','っれ':'rre','っろ':'rro','っわ':'wwa','ッか':d,'ッキ':e,'ック':h,'ッケ':i,'ッコ':j,'ッサ':k,'ッシ':l,'ッス':m,'ッセ':p,'ッソ':q,'ッタ':r,'ッチ':s,'ッツ':t,'ッテ':u,'ット':v,'ッパ':w,'ッピ':y,'ップ':z,'ッペ':'ppe','ッポ':'ppo','ッハ':'hha','ッヒ':'hhi','ッフ':'ffu','ッヘ':'hhe','ッホ':'hho','ッマ':'mma','ッミ':c,'ッム':'mmu','ッメ':'mme','ッモ':'mmo','ッヤ':'yya','ッユ':'yyu','ッヨ':'yyo','ッラ':'rra','ッリ':'rri','ッル':'rru','ッレ':'rre','ッロ':'rro','ッワ':'wwa','きゃ':'kya','きゅ':'kyu','きょ':'kyo','しゃ':'sha','しゅ':'shu','しょ':'sho','ちゃ':'cha','ちゅ':'chu','ちょ':'cho','にゃ':'nya','にゅ':'nyu','にょ':'nyo','ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','みゃ':'mya','みゅ':'myu','みょ':'myo','りゃ':'rya','りゅ':'ryu','りょ':'ryo','ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo','じゃ':'ja','じゅ':'ju','じょ':'jo','びゃ':'bya','びゅ':'byu','びょ':'byo','ぴゃ':'pya','ぴゅ':'pyu','ぴょ':'pyo','キャ':'kya','キュ':'kyu','キョ':'kyo','シャ':'sha','シュ':'shu','ショ':'sho','チャ':'cha','チュ':'chu','チョ':'cho','ニャ':'nya','ニュ':'nyu','ニョ':'nyo','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','ミャ':'mya','ミュ':'myu','ミョ':'myo','リャ':'rya','リュ':'ryu','リョ':'ryo','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ジャ':'ja','ジュ':'ju','ジョ':'jo','ビャ':'bya','ビュ':'byu','ビョ':'byo','ピャ':'pya','ピュ':'pyu','ピョ':'pyo','ああ':'aa','いい':'ii','うう':'uu','ええ':'ee','おお':'oo','おう':'oo',x:'-','は':B,'へ':C,'を':K,'あ':E,'い':M,'う':G,'え':C,'お':K,'か':N,'き':'ki','く':'ku','け':'ke','こ':'ko','さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to','な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':O,'ゆ':P,'よ':U,'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','わ':B,'ゐ':'wi','ゑ':'we','を':'wo','ん':'n','が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ざ':'za','じ':V,'ず':b,'ぜ':'ze','ぞ':'zo','だ':'da','ぢ':V,'づ':b,'で':'de','ど':'do','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ア':E,'イ':M,'ウ':G,'エ':C,'オ':K,'カ':N,'キ':'ki','ク':'ku','ケ':'ke','コ':'ko','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','マ':'ma','ミ':c,'ム':'mu','メ':'me','モ':'mo','ヤ':O,'ユ':P,'ヨ':U,'ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro','ワ':B,'ヰ':'wi','ヱ':'we','ヲ':'wo','ン':'n','ガ':'ga','ギ':'gi','グ':'gu','ゲ':'ge','ゴ':'go','ザ':'za','ジ':V,'ズ':b,'ゼ':'ze','ゾ':'zo','ダ':'da','ヂ':V,'ヅ':b,'デ':'de','ド':'do','バ':'ba','ビ':'bi','ブ':'bu','ベ':'be','ボ':'bo','パ':'pa','ピ':'pi','プ':'pu','ぺ':'pe','ポ':'po','ぁ':E,'ぃ':M,'ぅ':G,'ぇ':C,'ぉ':K,'ァ':E,'ィ':M,'ゥ':G,'ェ':C,'ォ':K,'ゃ':O,'ゅ':P,'ょ':U,'ャ':O,'ュ':P,'ョ':U,'ゎ':B,'ヮ':B,'ヶ':N,'ヵ':N};A.setup_styles();A.create_widgets();A.load_initial_data()
	def setup_styles(E):
		b='#666666';a='#0056b3';Z='Treeview';V='#000000';U='#dddddd';T='TButton';P='salmon';O='lightgreen';N='#e0e0e0';J='!disabled';H='active';G='#333333';D='#f0f0f0';B=A.Style();B.theme_use('clam');C=E.settings[I];K=E.settings[Q]
		if K==F:K=C
		L=E.settings[R]
		if L==F:L=C
		M=E.settings[S]
		if M==F:M=C
		B.configure('TFrame',background=D);B.configure('TLabel',background=D,foreground=G,font=(C,10));B.configure(T,font=(C,10),padding=6);B.map(T,background=[(H,N),(J,U)],foreground=[(H,V),(J,G)]);B.configure('Treeview.Heading',font=(C,10,k),background=N,foreground=G);B.configure(Z,font=(C,10),rowheight=25,background='#ffffff',foreground=G);B.map(Z,background=[('selected','#a8d8ff')]);B.configure(A8,font=(K,E.settings[W],k),foreground=a,background=D);B.configure(A9,font=(C,18),foreground=G,background=D);B.configure(AA,font=(C,12),foreground=b,background=D);B.configure(AB,font=(L,E.settings[X]),foreground=b,background=D);B.configure(AC,font=(M,E.settings[Y]),foreground='#888888',background=D);B.configure(AD,font=(C,20,k),foreground=a,background=D,wraplength=700);B.configure(l,font=(C,14),padding=10);B.map(l,background=[(H,N),(J,U)],foreground=[(H,V),(J,G)]);B.configure(AE,font=(C,14,k),background=D);B.configure(y,background=O,foreground=p);B.map(y,background=[(H,O),(J,O)]);B.configure(z,background=P,foreground=p);B.map(z,background=[(H,P),(J,P)]);B.configure('TCheckbutton',background=D,foreground=G,font=(C,10));B.configure('TCombobox',font=(C,10));B.configure('TSpinbox',font=(C,10))
	def create_widgets(B):B.main_frame=A.Frame(B.master,padding=h);B.main_frame.pack(fill=C.BOTH,expand=H);B.learning_frame=A.Frame(B.master,padding=h);B.progress_bar=A.Progressbar(B.learning_frame,orient='horizontal',mode='determinate');B.progress_bar.pack(fill=C.X,pady=5);B.create_main_page_widgets();B.create_direct_learning_widgets();B.create_quiz_widgets()
	def create_main_page_widgets(B):G='definition';F='word';A.Label(B.main_frame,text='MemoWord 词汇表',font=(B.settings[I],18,k)).pack(pady=15);B.total_study_label=A.Label(B.main_frame,text='进入学习界面次数: 0',font=(B.settings[I],12));B.total_study_label.pack(pady=5);B.vocab_tree=A.Treeview(B.main_frame,columns=(F,G,O,U),show='headings');B.vocab_tree.heading(F,text='词汇');B.vocab_tree.heading(G,text='解释');B.vocab_tree.heading(O,text='学习次数');B.vocab_tree.heading(U,text='上次学习时间');B.vocab_tree.column(F,width=150,minwidth=100,anchor=P);B.vocab_tree.column(G,width=300,minwidth=200,anchor=D);B.vocab_tree.column(O,width=100,minwidth=80,anchor=P);B.vocab_tree.column(U,width=150,minwidth=120,anchor=P);B.vocab_tree.pack(fill=C.BOTH,expand=H,pady=10);J=A.Scrollbar(B.vocab_tree,orient='vertical',command=B.vocab_tree.yview);J.pack(side='right',fill='y');B.vocab_tree.configure(yscrollcommand=J.set);E=A.Frame(B.main_frame);E.pack(pady=15);B.import_button=A.Button(E,text='导入词汇表',command=B.load_vocabulary);B.import_button.pack(side=C.LEFT,padx=10);B.start_learning_button=A.Button(E,text=q,command=B.start_learning);B.start_learning_button.pack(side=C.LEFT,padx=10);B.settings_button=A.Button(E,text='设置',command=B.open_settings);B.settings_button.pack(side=C.LEFT,padx=10)
	def create_direct_learning_widgets(B):B.direct_learning_sub_frame=A.Frame(B.learning_frame,padding=h);B.learning_romaji_label=A.Label(B.direct_learning_sub_frame,text=G,style=AC,wraplength=700,anchor=P);B.learning_romaji_label.pack(pady=(20,0),fill=C.X);B.learning_word_label=A.Label(B.direct_learning_sub_frame,text=G,style=A8,wraplength=700,anchor=P);B.learning_word_label.pack(pady=(5,0),fill=C.X);B.learning_bracketed_label=A.Label(B.direct_learning_sub_frame,text=G,style=AB,wraplength=700,anchor=P);B.learning_bracketed_label.pack(pady=(5,20),fill=C.X);B.learning_definition_label=A.Label(B.direct_learning_sub_frame,text=G,style=A9,wraplength=700,anchor=P);B.learning_definition_label.pack(pady=20,fill=C.X);B.learning_similar_label=A.Label(B.direct_learning_sub_frame,text=G,style=AA,wraplength=700,anchor=P);B.learning_similar_label.pack(pady=10,fill=C.X);D=A.Frame(B.direct_learning_sub_frame);D.pack(pady=30);B.reveal_button=A.Button(D,text='显示解释',command=B.reveal_definition);B.reveal_button.pack(side=C.LEFT,padx=15);B.next_word_button=A.Button(D,text='下一个',command=B.next_direct_word,state=C.DISABLED);B.next_word_button.pack(side=C.LEFT,padx=15);B.back_to_main_button_direct=A.Button(B.direct_learning_sub_frame,text='返回主页',command=B.show_main_page);B.back_to_main_button_direct.pack(pady=20)
	def create_quiz_widgets(B):
		B.quiz_sub_frame=A.Frame(B.learning_frame,padding=h);B.quiz_question_label=A.Label(B.quiz_sub_frame,text=G,style=AD,anchor=P);B.quiz_question_label.pack(pady=40,fill=C.X);B.quiz_options_frame=A.Frame(B.quiz_sub_frame);B.quiz_options_frame.pack(pady=20,fill=C.X,expand=H);B.quiz_options_frame.grid_columnconfigure(0,weight=1);B.quiz_options_frame.grid_columnconfigure(1,weight=1);B.quiz_option_buttons=[]
		for D in r(4):E=A.Button(B.quiz_options_frame,text=f"Option {D+1}",style=l,command=lambda i=D:B.check_quiz_answer(B.quiz_option_buttons[i][A0]));E.grid(row=D//2,column=D%2,padx=10,pady=10,sticky=b);B.quiz_option_buttons.append(E)
		B.quiz_feedback_label=A.Label(B.quiz_sub_frame,text=G,style=AE);B.quiz_feedback_label.pack(pady=15);B.quiz_next_button=A.Button(B.quiz_sub_frame,text='下一个问题',command=B.next_quiz_question,state=C.DISABLED);B.quiz_next_button.pack(pady=10);B.back_to_main_button_quiz=A.Button(B.quiz_sub_frame,text='返回主页',command=B.show_main_page);B.back_to_main_button_quiz.pack(pady=20)
	def show_main_page(A):A.learning_frame.pack_forget();A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack_forget();A.main_frame.pack(fill=C.BOTH,expand=H);A.update_main_page_display()
	def show_learning_page(A,mode):
		A.main_frame.pack_forget();A.learning_frame.pack(fill=C.BOTH,expand=H);A.progress_bar.config(value=0)
		if mode==AF:A.quiz_sub_frame.pack_forget();A.direct_learning_sub_frame.pack(fill=C.BOTH,expand=H)
		elif mode=='quiz':A.direct_learning_sub_frame.pack_forget();A.quiz_sub_frame.pack(fill=C.BOTH,expand=H)
	def load_initial_data(A):A.load_progress();A.update_main_page_display()
	def load_vocabulary(F):
		P=AI.askopenfilename(filetypes=[('JSON files','*.json')])
		if not P:return
		try:
			with s(P,'r',encoding=A1)as V:Q=i.load(V)
			J={A[D]:A for A in F.vocabulary_data};L=[]
			for A in Q:
				H=A.get(D)
				if not H:continue
				if H in J:C=J[H];C[N]=A.get(N,C.get(N,G));C[K]=A.get(K,C.get(K,[]));C[M]=A.get(M,C.get(M,0));L.append(C)
				else:L.append({M:A.get(M,0),D:H,N:A.get(N,G),K:A.get(K,[]),O:0,U:g})
			I={}
			for R in L:I[R[D]]=R
			for(S,W)in J.items():
				if S not in I:I[S]=W
			F.vocabulary_data=e(I.values());F.vocabulary_data.sort(key=lambda x:x.get(M,0));F.save_progress();F.update_main_page_display();E.showinfo('导入成功',f"成功导入 {B(Q)} 个词汇。")
		except i.JSONDecodeError:E.showerror(c,'无效的JSON文件格式。请确保文件内容符合JSON规范。')
		except m as T:E.showerror(c,f"导入词汇时发生错误: {T}");print(f"Error during import: {T}")
		finally:F.master.focus_set()
	def load_progress(A):
		if os.path.exists(A.progress_file):
			try:
				with s(A.progress_file,'r',encoding=A1)as C:
					B=i.load(C)
					if isinstance(B,dict)and A2 in B:A.vocabulary_data=B.get(A2,[]);A.session_start_count=B.get(AG,0);A.settings.update(B.get(AH,{}))
					else:A.vocabulary_data=B;A.session_start_count=0
			except i.JSONDecodeError:E.showerror(c,'学习进度文件损坏或格式不正确，将重新创建。');A.vocabulary_data=[];A.session_start_count=0;A.settings={I:n,f:o,Q:F,W:36,R:F,X:20,S:F,Y:14,J:a,L:H,Z:T}
			except m as D:E.showerror(c,f"加载学习进度时发生错误: {D}");A.vocabulary_data=[];A.session_start_count=0;A.settings={I:n,f:o,Q:F,W:36,R:F,X:20,S:F,Y:14,J:a,L:H,Z:T}
		else:A.vocabulary_data=[];A.session_start_count=0;A.settings={I:n,f:o,Q:F,W:36,R:F,X:20,S:F,Y:14,J:a,L:H,Z:T}
	def save_progress(A):
		try:
			B={A2:A.vocabulary_data,AG:A.session_start_count,AH:A.settings}
			with s(A.progress_file,D,encoding=A1)as C:i.dump(B,C,ensure_ascii=T,indent=4)
		except m as F:E.showerror(c,f"保存学习进度时发生错误: {F}")
	def update_main_page_display(A):
		for H in A.vocab_tree.get_children():A.vocab_tree.delete(H)
		for B in A.vocabulary_data:
			I=B.get(D,A3);J=B.get(N,A3);K=B.get(O,0);F=B.get(U);E='未学习'
			if F:
				try:L=j.fromisoformat(F);E=L.strftime('%Y-%m-%d %H:%M')
				except t:E='日期格式错误'
			A.vocab_tree.insert(G,C.END,values=(I,J,K,E))
		A.total_study_label.config(text=f"进入学习界面次数: {A.session_start_count}")
	def start_learning(A):
		if not A.vocabulary_data:E.showwarning('提示','请先导入词汇表！');return
		A.session_start_count+=1;A.save_progress();F=[];D=[];G=[];J=j.now();K=J-AJ(days=3)
		for C in A.vocabulary_data:
			H=C.get(O,0);I=C.get(U)
			if H==0:F.append(C)
			elif I:
				try:
					N=j.fromisoformat(I)
					if H<15 and N<K:D.append(C)
					else:G.append(C)
				except t:D.append(C)
			else:D.append(C)
		F.sort(key=lambda x:x.get(M,0))
		if D:
			if A.settings[L]:E.showinfo(q,f"有 {B(D)} 个单词需要优先复习！")
			A.start_quiz_session(D)
		elif A.recently_learned_for_quiz:
			if A.settings[L]:E.showinfo('开始复习',f"开始复习刚刚学习的 {B(A.recently_learned_for_quiz)} 个单词！")
			P=e(A.recently_learned_for_quiz);A.recently_learned_for_quiz.clear();A.start_quiz_session(P)
		elif F:
			A.direct_learning_session=F[:5]
			if A.settings[L]:E.showinfo(q,f"开始学习 {B(A.direct_learning_session)} 个新单词！")
			A.start_direct_learning_session()
		else:
			if not G:E.showinfo('恭喜','所有单词都已学习或复习完毕！');return
			V.shuffle(G);A.quiz_session_words=G[:10]
			if A.settings[L]:E.showinfo(q,f"开始复习 {B(A.quiz_session_words)} 个旧单词！")
			A.start_quiz_session(A.quiz_session_words)
		A.master.focus_set()
	def start_direct_learning_session(A):
		A.direct_word_index=0
		if A.direct_learning_session:A.show_learning_page(AF);A.progress_bar.config(maximum=B(A.direct_learning_session),value=0);A.display_current_direct_word()
		else:A.show_main_page()
	def _kana_to_romaji(F,kana_text):
		C=kana_text;D=[];A=0
		while A<B(C):
			K=T
			for J in r(3,0,-1):
				if A+J<=B(C):
					E=C[A:A+J]
					if E in F.KANA_TO_ROMAJI_MAP:
						if E==x and D:
							L=re.search('[aeiou]$',D[-1])
							if L:D[-1]+=L.group(0)
							else:D.append('-')
						elif E in['ん','ン']and A+1<B(C)and re.match('[あいうえおやゆよアイウエオヤユヨ]',C[A+1]):D.append("n'")
						elif E in['っ','ッ']and A+1<B(C):
							I=g
							for M in r(3,0,-1):
								if A+1+M<=B(C):
									N=C[A+1:A+1+M]
									if N in F.KANA_TO_ROMAJI_MAP:I=F.KANA_TO_ROMAJI_MAP[N];break
							if I and I[0].isalpha():D.append(I[0])
						else:D.append(F.KANA_TO_ROMAJI_MAP[E])
						A+=J;K=H;break
			if not K:D.append(C[A]);A+=1
		return G.join(D)
	def display_current_direct_word(A):
		P="点击 '显示解释' 查看"
		if A.direct_word_index<B(A.direct_learning_session):
			I=A.direct_learning_session[A.direct_word_index];F=I.get(D,G);A.progress_bar.config(value=A.direct_word_index+1)
			if A.settings[Z]:Q=G.join(A for A in F if'\u3040'<=A<='ゟ'or'゠'<=A<='ヿ'or A==x);R=A._kana_to_romaji(Q);A.learning_romaji_label.config(text=R)
			else:A.learning_romaji_label.config(text=G)
			M=re.search('〔.*?〕',F)
			if M:N=M.group(0);S=F.replace(N,G).strip();A.learning_word_label.config(text=S);A.learning_bracketed_label.config(text=N)
			else:A.learning_word_label.config(text=F);A.learning_bracketed_label.config(text=G)
			H=A.settings[J]
			if H==A4:A.learning_definition_label.config(text=G,foreground=p)
			elif H==a:A.learning_definition_label.config(text=P,foreground='gray')
			elif H==A5:A.learning_definition_label.config(text=P,foreground='blue')
			O=', '.join(I.get(K,[]));A.learning_similar_label.config(text=f"形近/音近词: {O}"if O else'无形近/音近词');A.reveal_button.config(state=C.NORMAL);A.next_word_button.config(state=C.DISABLED)
		elif A.direct_learning_session:
			A.recently_learned_for_quiz=e(A.direct_learning_session)
			if A.settings[L]:E.showinfo('学习完成',f"本次新词学习已完成！接下来将复习刚刚学习的 {B(A.recently_learned_for_quiz)} 个单词。")
			A.start_quiz_session(A.recently_learned_for_quiz)
		else:E.showinfo('学习结束','本次学习已完成！');A.show_main_page()
	def reveal_definition(A):
		if A.direct_word_index<B(A.direct_learning_session):
			E=A.direct_learning_session[A.direct_word_index];A.learning_definition_label.config(text=E.get(N,'无解释'),foreground=p);A.reveal_button.config(state=C.DISABLED);A.next_word_button.config(state=C.NORMAL);H=E.get(D)
			for(F,G)in u(A.vocabulary_data):
				if G.get(D)==H:A.vocabulary_data[F][O]=G.get(O,0)+1;A.vocabulary_data[F][U]=j.now().isoformat();break
			A.save_progress()
	def next_direct_word(A):A.direct_word_index+=1;A.display_current_direct_word()
	def start_quiz_session(A,words_to_quiz=g):
		C=words_to_quiz;A.incorrectly_answered_words=[];A.quiz_items_completed=0
		if C is not g:A.quiz_words_to_ask=e(C);A.quiz_total_items_to_complete=B(C)
		else:A.quiz_words_to_ask=e(A.quiz_session_words);A.quiz_total_items_to_complete=B(A.quiz_session_words)
		V.shuffle(A.quiz_words_to_ask)
		if A.quiz_words_to_ask:A.show_learning_page('quiz');A.progress_bar.config(maximum=A.quiz_total_items_to_complete,value=A.quiz_items_completed);A.display_quiz_question()
		else:E.showinfo('测验结束','本次测验已完成！');A.show_main_page()
	def display_quiz_question(A):
		S='meaning_to_word';A.quiz_feedback_label.config(text=G)
		for I in A.quiz_option_buttons:I.config(state=C.NORMAL,style=l)
		A.quiz_next_button.config(state=C.DISABLED)
		if A.incorrectly_answered_words:A.current_quiz_word=A.incorrectly_answered_words.pop(0)
		elif A.quiz_words_to_ask:A.current_quiz_word=A.quiz_words_to_ask.pop(0)
		else:E.showinfo('测验结束','恭喜！所有题目都已答对！');A.show_main_page();return
		T=V.choice([S,'word_to_meaning']);F=[];H=G
		if T==S:
			J=f"请选择与 '{A.current_quiz_word.get(N,"无解释")}' 对应的单词：";H=A.current_quiz_word.get(D);F.append(H);L=[A for A in A.current_quiz_word.get(K,[])if A!=H];V.shuffle(L);M=[A[D]for A in A.vocabulary_data if A[D]!=H];V.shuffle(M)
			for O in L:
				if B(F)<4 and O not in F:F.append(O)
			for P in M:
				if B(F)<4 and P not in F:F.append(P)
			while B(F)<4:F.append(f"选项 {B(F)+1}")
		else:
			J=f"请选择 '{A.current_quiz_word.get(D,A3)}' 的正确解释：";H=A.current_quiz_word.get(N);F.append(H);Q=[A[N]for A in A.vocabulary_data if A[N]!=H];V.shuffle(Q)
			for R in Q:
				if B(F)<4 and R not in F:F.append(R)
			while B(F)<4:F.append(f"解释 {B(F)+1}")
		V.shuffle(F);A.current_quiz_correct_answer=H;A.quiz_question_label.config(text=J)
		for(U,I)in u(A.quiz_option_buttons):I.config(text=F[U])
	def check_quiz_answer(A,selected_answer):
		E=selected_answer;F=E==A.current_quiz_correct_answer
		if F:A.quiz_feedback_label.config(text='正确！',foreground='green');A.quiz_items_completed+=1
		else:
			A.quiz_feedback_label.config(text=f"错误！正确答案是: {A.current_quiz_correct_answer}",foreground='red')
			if A.current_quiz_word not in A.incorrectly_answered_words:A.incorrectly_answered_words.append(A.current_quiz_word)
		I=A.current_quiz_word.get(D)
		for(G,H)in u(A.vocabulary_data):
			if H.get(D)==I:A.vocabulary_data[G][O]=H.get(O,0)+1;A.vocabulary_data[G][U]=j.now().isoformat();break
		A.save_progress();A.progress_bar.config(value=A.quiz_items_completed)
		for B in A.quiz_option_buttons:
			B.config(state=C.DISABLED)
			if B[A0]==A.current_quiz_correct_answer:B.config(style=y)
			elif B[A0]==E and not F:B.config(style=z)
			else:B.config(style=l)
		A.quiz_next_button.config(state=C.NORMAL)
	def next_quiz_question(A):A.display_quiz_question()
	def open_settings(B):
		O='readonly';K=C.Toplevel(B.master);K.title('设置');K.geometry('500x450');K.resizable(T,T);K.transient(B.master);K.grab_set();K.focus_set();P=A.Notebook(K);P.pack(pady=10,padx=10,fill=C.BOTH,expand=H);N=A.Frame(P,padding=h);P.add(N,text='显示设置');G=A.Frame(P,padding=h);P.add(G,text='字体设置');U=sorted(e(font.families()));V=[d]+U;M=0;A.Label(N,text='解释提示样式:').grid(row=M,column=0,padx=5,pady=5,sticky=D);B.reveal_hint_style_var=C.StringVar(value=B.settings[J])
		if B.settings[J]==A4:B.reveal_hint_style_var.set(A6)
		elif B.settings[J]==a:B.reveal_hint_style_var.set('低调')
		elif B.settings[J]==A5:B.reveal_hint_style_var.set('明显')
		j=[A6,'低调','明显'];k=A.Combobox(N,textvariable=B.reveal_hint_style_var,values=j,state=O);k.grid(row=M,column=1,padx=5,pady=5,sticky=b);M+=1;A.Label(N,text='学习概述:').grid(row=M,column=0,padx=5,pady=5,sticky=D);B.show_session_summary_var=C.BooleanVar(value=B.settings[L]);A.Checkbutton(N,text='显示学习内容概述',variable=B.show_session_summary_var).grid(row=M,column=1,padx=5,pady=5,sticky=D);M+=1;A.Label(N,text='日语罗马音:').grid(row=M,column=0,padx=5,pady=5,sticky=D);B.show_romaji_for_kana_var=C.BooleanVar(value=B.settings[Z]);A.Checkbutton(N,text='显示日语假名罗马音',variable=B.show_romaji_for_kana_var).grid(row=M,column=1,padx=5,pady=5,sticky=D);M+=1;N.grid_columnconfigure(1,weight=1);E=0;A.Label(G,text='全局界面字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);B.global_font_family_var=C.StringVar(value=B.settings[I]);l=A.Combobox(G,textvariable=B.global_font_family_var,values=U,state=O);l.grid(row=E,column=1,padx=5,pady=5,sticky=b);E+=1;A.Label(G,text='备用字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);B.fallback_font_family_var=C.StringVar(value=B.settings[f]);m=A.Combobox(G,textvariable=B.fallback_font_family_var,values=U,state=O);m.grid(row=E,column=1,padx=5,pady=5,sticky=b);E+=1;A.Label(G,text='主单词字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);c=B.settings[Q]
		if c==F or c==B.settings[I]:B.main_word_font_family_var=C.StringVar(value=d)
		else:B.main_word_font_family_var=C.StringVar(value=c)
		n=A.Combobox(G,textvariable=B.main_word_font_family_var,values=V,state=O);n.grid(row=E,column=1,padx=5,pady=5,sticky=b);E+=1;A.Label(G,text='主单词大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);B.main_word_font_size_var=C.StringVar(value=v(B.settings[W]));o=A.Spinbox(G,from_=10,to_=72,textvariable=B.main_word_font_size_var,width=5);o.grid(row=E,column=1,padx=5,pady=5,sticky=D);E+=1;A.Label(G,text='括号文字字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);g=B.settings[R]
		if g==F or g==B.settings[I]:B.bracketed_font_family_var=C.StringVar(value=d)
		else:B.bracketed_font_family_var=C.StringVar(value=g)
		p=A.Combobox(G,textvariable=B.bracketed_font_family_var,values=V,state=O);p.grid(row=E,column=1,padx=5,pady=5,sticky=b);E+=1;A.Label(G,text='括号文字大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);B.bracketed_font_size_var=C.StringVar(value=v(B.settings[X]));q=A.Spinbox(G,from_=8,to_=48,textvariable=B.bracketed_font_size_var,width=5);q.grid(row=E,column=1,padx=5,pady=5,sticky=D);E+=1;A.Label(G,text='罗马音字体:').grid(row=E,column=0,padx=5,pady=5,sticky=D);i=B.settings[S]
		if i==F or i==B.settings[I]:B.romaji_font_family_var=C.StringVar(value=d)
		else:B.romaji_font_family_var=C.StringVar(value=i)
		r=A.Combobox(G,textvariable=B.romaji_font_family_var,values=V,state=O);r.grid(row=E,column=1,padx=5,pady=5,sticky=b);E+=1;A.Label(G,text='罗马音大小:').grid(row=E,column=0,padx=5,pady=5,sticky=D);B.romaji_font_size_var=C.StringVar(value=v(B.settings[Y]));s=A.Spinbox(G,from_=8,to_=48,textvariable=B.romaji_font_size_var,width=5);s.grid(row=E,column=1,padx=5,pady=5,sticky=D);E+=1;G.grid_columnconfigure(1,weight=1);A.Button(K,text='保存设置',command=lambda:B.save_settings(K)).pack(pady=10);K.protocol('WM_DELETE_WINDOW',lambda:B.on_settings_close(K))
	def on_settings_close(B,settings_window):A=settings_window;A.grab_release();A.destroy()
	def save_settings(A,settings_window):
		try:
			A.settings[I]=A.global_font_family_var.get();A.settings[f]=A.fallback_font_family_var.get();C=A.main_word_font_family_var.get()
			if C==d:A.settings[Q]=F
			else:A.settings[Q]=C
			A.settings[W]=w(A.main_word_font_size_var.get());D=A.bracketed_font_family_var.get()
			if D==d:A.settings[R]=F
			else:A.settings[R]=D
			A.settings[X]=w(A.bracketed_font_size_var.get());G=A.romaji_font_family_var.get()
			if G==d:A.settings[S]=F
			else:A.settings[S]=G
			A.settings[Y]=w(A.romaji_font_size_var.get());B=A.reveal_hint_style_var.get()
			if B==A6:A.settings[J]=A4
			elif B=='低调':A.settings[J]=a
			elif B=='明显':A.settings[J]=A5
			A.settings[L]=A.show_session_summary_var.get();A.settings[Z]=A.show_romaji_for_kana_var.get();A.save_progress();A.setup_styles();E.showinfo('设置','设置已保存！');A.on_settings_close(settings_window)
		except t:E.showerror(c,'字体大小必须是整数！')
		except m as H:E.showerror(c,f"保存设置时发生错误: {H}")
if __name__=='__main__':A7=C.Tk();AL=AK(A7);A7.mainloop()