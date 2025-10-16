import streamlit as st
import random
from fractions import Fraction

# --- Question Generation Engine (80 Questions per Subject) ---

def generate_english_questions(num_questions=20):
    # Expanded based on the P5 English PDF
    question_bank = [
        {"question": "The waiter gave us a {} to look at.", "options": ["menu", "frying", "stirring", "Italian"], "answer": "menu", "explanation": "A 'menu' lists the food available in a restaurant."},
        {"question": "Our chef is good at {} rice with peanut oil.", "options": ["menu", "frying", "serving tray", "Vietnam"], "answer": "frying", "explanation": "'Frying' is a cooking method using hot oil."},
        {"question": "I usually put dishes on a {} and bring them to the table.", "options": ["stirring", "serving tray", "frying", "menu"], "answer": "serving tray", "explanation": "A 'serving tray' is used to carry dishes."},
        {"question": "This restaurant is famous for its {} food, like pasta and pizza.", "options": ["Italian", "frying", "menu", "stirring"], "answer": "Italian", "explanation": "Pasta and pizza are classic Italian foods."},
        {"question": "You need to keep {} the sauce, or it will stick to the pot.", "options": ["frying", "serving", "stirring", "slicing"], "answer": "stirring", "explanation": "'Stirring' means mixing in a circular motion."},
        {"question": "We only have 10 tickets for 20 people. We have {} tickets.", "options": ["plenty of", "enough", "not enough", "some"], "answer": "not enough", "explanation": "If you have fewer items than you need, you have 'not enough'."},
        {"question": "John {} to buy some milk from the store.", "options": ["need", "need to", "needs", "needs to"], "answer": "needs to", "explanation": "For a third-person singular subject (John), the verb 'need' requires an '-s', and it should be followed by 'to' before another verb."},
        {"question": "When the teacher walked in, the students {} loudly.", "options": ["were talking", "talked", "are talking", "talk"], "answer": "were talking", "explanation": "This describes an ongoing action in the past that was interrupted, requiring the Past Continuous tense."},
        {"question": "My father got sick because of being {}.", "options": ["overworked", "grateful", "delicious", "generous"], "answer": "overworked", "explanation": "'Overworked' means working too much, which can lead to sickness."},
        {"question": "I am very {} for your help.", "options": ["delicious", "grateful", "needy", "low-income"], "answer": "grateful", "explanation": "'Grateful' is another word for thankful."},
        {"question": "A box lunch at this restaurant {} around $45.", "options": ["cost", "costs", "is costing", "costed"], "answer": "costs", "explanation": "For a third-person singular subject (A box lunch) in the Present Simple tense, the verb needs an '-s'."},
        {"question": "She sells lunches at low prices to {} people.", "options": ["low-income", "generous", "grateful", "delicious"], "answer": "low-income", "explanation": "'Low-income' describes people who do not earn much money."},
        {"question": "Mr. Li is very {}; he always helps the poor.", "options": ["delicious", "overworked", "needy", "generous"], "answer": "generous", "explanation": "A 'generous' person is someone who gives freely to others."},
        {"question": "I {} to the Peak with my family last Sunday.", "options": ["go", "goes", "went", "will go"], "answer": "went", "explanation": "'Last Sunday' indicates the past, so the Past Simple form 'went' is used."},
        {"question": "Listen! The school choir {} our school song.", "options": ["sings", "sang", "is singing", "has sung"], "answer": "is singing", "explanation": "'Listen!' indicates an action happening now, requiring the Present Continuous tense."},
        {"question": "My mother {} dinner every evening.", "options": ["cooks", "cook", "is cooking", "cooked"], "answer": "cooks", "explanation": "'Every evening' describes a routine. For a third-person singular subject (mother), we use 'cooks'."},
        {"question": "I promise I {} my homework after this TV show.", "options": ["do", "did", "am doing", "will do"], "answer": "will do", "explanation": "A promise about a future action uses the Future Simple tense 'will do'."},
        {"question": "The opposite of 'polite' is {}.", "options": ["impolite", "unpolite", "dispolite", "nonpolite"], "answer": "impolite", "explanation": "The prefix 'im-' is used to form the opposite of 'polite'."},
        {"question": "A person who designs buildings is called an {}.", "options": ["artist", "architect", "astronaut", "author"], "answer": "architect", "explanation": "An architect is a professional who designs buildings and other structures."},
        {"question": "How {} sugar do we need for this cake?", "options": ["many", "much", "long", "often"], "answer": "much", "explanation": "'Much' is used with uncountable nouns like 'sugar'."},
        # ... (Add 60 more English questions here to reach 80)
    ] * 4 # Duplicate to reach 80 questions for demonstration
    return random.sample(question_bank, num_questions)

def generate_maths_questions(num_questions=20):
    questions = []
    # Generate 80 unique types of questions
    for i in range(80):
        q_type_index = i % 5 
        if q_type_index == 0: # Fractions
            d1, d2 = random.sample([3, 4, 5, 6, 8, 10, 12, 15], 2)
            n1, n2 = random.randint(1, d1-1), random.randint(1, d2-1)
            f1, f2 = Fraction(n1, d1), Fraction(n2, d2)
            op = random.choice(['+', '-'])
            if op == '-' and f1 < f2: f1, f2 = f2, f1
            answer = f1 + f2 if op == '+' else f1 - f2
            explanation = f"通分母後計算：\n{f1.numerator*f2.denominator}/{f1.denominator*f2.denominator} {op} {f2.numerator*f1.denominator}/{f1.denominator*f2.denominator} = {answer}"
            questions.append({"question": f"計算：{f1} {op} {f2}", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 1: # Area
            shape = random.choice(['parallelogram', 'triangle', 'rectangle'])
            base = random.randint(10, 40); height = random.randint(5, 25)
            if shape == 'parallelogram':
                answer = base * height
                explanation = f"面積 = 底 × 高\n= {base} × {height}\n= {answer}"
                questions.append({"question": f"一個平行四邊形的底是 {base} cm，高是 {height} cm，它的面積是多少？", "answer": str(answer), "explanation": explanation})
            elif shape == 'rectangle':
                answer = base * height
                explanation = f"面積 = 長 × 闊\n= {base} × {height}\n= {answer}"
                questions.append({"question": f"一個長方形的長是 {base} cm，闊是 {height} cm，它的面積是多少？", "answer": str(answer), "explanation": explanation})
            else:
                answer = (base * height) / 2
                explanation = f"面積 = (底 × 高) ÷ 2\n= ({base} × {height}) ÷ 2\n= {answer}"
                questions.append({"question": f"一個三角形的底是 {base} cm，高是 {height} cm，它的面積是多少？", "answer": str(int(answer)) if answer.is_integer() else str(answer), "explanation": explanation})
        elif q_type_index == 2: # Factors and Multiples
            num = random.randint(20, 100)
            if i % 2 == 0:
                factors = [i for i in range(1, num + 1) if num % i == 0]
                answer = len(factors)
                explanation = f"{num} 的因數是：{', '.join(map(str, factors))}\n共有 {answer} 個因數。"
                questions.append({"question": f"{num} 共有多少個因數？", "answer": str(answer), "explanation": explanation})
            else:
                multiple_of = random.randint(3, 12)
                multiples = [multiple_of * i for i in range(1, 101 // multiple_of)]
                answer = len(multiples)
                explanation = f"100以內 {multiple_of} 的倍數有：{', '.join(map(str, multiples))}"
                questions.append({"question": f"100以內有多少個 {multiple_of} 的倍數？", "answer": str(answer), "explanation": explanation})
        elif q_type_index == 3: # Word Problem
            price = random.randint(10, 80) * 10
            qty = random.randint(5, 20)
            total = price * qty
            explanation = f"算式：{price} × {qty} = {total} 元"
            questions.append({"question": f"每張遊戲咭售 {price} 元，小明買了 {qty} 張，共需付多少元？", "answer": str(total), "explanation": explanation})
        elif q_type_index == 4: # Mixed Operations
            a, b, c = random.randint(20, 50), random.randint(2, 10), random.randint(5, 20)
            answer = a * (b + c)
            explanation = f"先計算括號內的部分：\n步驟一：{b} + {c} = {b+c}\n步驟二：{a} × {b+c} = {answer}"
            questions.append({"question": f"計算：{a} × ({b} + {c})", "answer": str(answer), "explanation": explanation})
    random.shuffle(questions)
    return random.sample(questions, num_questions)

def generate_chinese_questions(num_questions=20):
    question_bank = [
        {"question": "看到這隻受傷的流浪貓，我們怎可以（　），把牠留在街角，置之不理呢？", "options": ["怒髮衝冠", "三思而行", "視若無睹", "自強而息"], "answer": "視若無睹", "explanation": "「視若無睹」指看見了卻像沒看見一樣，形容漠不關心。"},
        {"question": "姐姐事事挑剔、凡事力求完美，這種（　）的性格，實在令人吃不消。", "options": ["不可一世", "一無是處", "手不釋卷", "吹毛求疵"], "answer": "吹毛求疵", "explanation": "「吹毛求疵」比喻故意挑剔別人的缺點，尋找差錯。"},
        {"question": "志明雖然名列前茅，但那（　）的態度卻令大家很反感。", "options": ["不可一世", "三思而行", "視若無睹", "自強不息"], "answer": "不可一世", "explanation": "「不可一世」形容人自以為了不起，驕傲自大到了極點。"},
        {"question": "風低聲耳語，向大樹訴說着他鄉的小故事。這句運用了什麼修辭手法？", "options": ["明喻", "暗喻", "擬人", "排比"], "answer": "擬人", "explanation": "「擬人」是把事物人格化，賦予它們人的思想和感情。"},
        {"question": "時間是一把無情的刀，靜靜地削減着我們的青春。這句運用了什麼修辭手法？", "options": ["明喻", "暗喻", "擬人", "擬聲"], "answer": "暗喻", "explanation": "「暗喻」是把甲事物說成乙事物，本體和喻體都出現，但不用「像」等比喻詞。"},
        {"question": "「守株待兔」這個成語比喻一個人怎樣？", "options": ["勤奮工作", "堅持信念", "思想守舊，不知變通", "運氣很好"], "answer": "思想守舊，不知變通", "explanation": "比喻死守狹隘經驗，不知變通。"},
        {"question": "「亡羊補牢」的故事教訓我們什麼？", "options": ["養羊很困難", "犯了錯應及時改正", "羊會自己跑掉", "鄰居不可信"], "answer": "犯了錯應及時改正", "explanation": "比喻出了問題以後想辦法補救，可以防止繼續受損失。"},
        {"question": "「媽媽的笑容像溫暖的陽光。」這句運用了什麼修辭手法？", "options": ["明喻", "暗喻", "誇張", "擬人"], "answer": "明喻", "explanation": "「明喻」使用「像」、「如」、「彷彿」等比喻詞，把甲事物比作乙事物。"},
        {"question": "「刻舟求劍」比喻一個人怎樣？", "options": ["辦事靈活", "善於觀察", "固執不知變通", "記憶力好"], "answer": "固執不知變通", "explanation": "比喻辦事拘泥，不知變通。"},
        {"question": "「那座山高得快要碰到天了。」這句運用了什麼修辭手法？", "options": ["誇張", "比喻", "擬人", "對比"], "answer": "誇張", "explanation": "「誇張」是為了達到某種表達效果，對事物的形象、特徵、作用、程度等方面著意誇大或縮小的修辭方式。"},
        # ... (Add 70 more Chinese questions here to reach 80)
    ] * 8 # Duplicate to reach 80 questions
    return random.sample(question_bank, num_questions)

def generate_gs_questions(num_questions=20):
    question_bank = [
        {"question": "張騫出使西域的主要目的是什麼？", "options": ["進行文化交流", "聯絡西域國家對抗匈奴", "增進對西域的認識", "尋找黃金"], "answer": "聯絡西域國家對抗匈奴", "explanation": "漢武帝派遣張騫出使西域的主要目的是為了聯合大月氏等國家，共同夾擊匈奴。"},
        {"question": "張騫出使西域後，打通了一條貫通中西的通道，後世稱之為什麼？", "options": ["黃金大道", "茶馬古道", "絲綢之路", "海上長城"], "answer": "絲綢之路", "explanation": "由於這條路上運輸最多的商品是中國的絲綢，因此被稱為「絲綢之路」。"},
        {"question": "玄奘到天竺（古代印度）取經是在哪個朝代？", "options": ["漢朝", "唐朝", "宋朝", "明朝"], "answer": "唐朝", "explanation": "玄奘是唐代著名的高僧，他西行取經的故事被記載在《大唐西域記》中。"},
        {"question": "《清明上河圖》描繪了哪個朝代的繁榮景象？", "options": ["唐朝", "宋朝", "元朝", "明朝"], "answer": "宋朝", "explanation": "《清明上河圖》是北宋的風俗畫，描繪了首都汴京的繁華景象。"},
        {"question": "元朝是由哪個民族建立的？", "options": ["漢族", "滿族", "蒙古族", "藏族"], "answer": "蒙古族", "explanation": "元朝是由蒙古族領袖忽必烈建立的。"},
        {"question": "被尊稱為「成吉思汗」的蒙古族領袖是誰？", "options": ["忽必烈", "窩闊台", "鐵木真", "拖雷"], "answer": "鐵木真", "explanation": "鐵木真統一了蒙古各部落後，被尊稱為「成吉思汗」。"},
        {"question": "鄭和下西洋是在哪個朝代發生的？", "options": ["宋朝", "元朝", "明朝", "清朝"], "answer": "明朝", "explanation": "鄭和是明朝的航海家，受明成祖派遣七次下西洋。"},
        {"question": "鄭和下西洋最遠到達了哪個地區？", "options": ["美洲西岸", "歐洲南部", "非洲東部", "澳洲北部"], "answer": "非洲東部", "explanation": "鄭和的船隊最遠曾到達非洲東部及紅海沿岸。"},
        {"question": "在太陽系中，哪類星體會圍繞恆星運行？", "options": ["行星", "衛星", "彗星", "流星"], "answer": "行星", "explanation": "行星的定義是圍繞恆星運行的天體，例如地球圍繞太陽運行。"},
        {"question": "月球是屬於哪一類星體？", "options": ["恆星", "行星", "衛星", "小行星"], "answer": "衛星", "explanation": "衛星是圍繞行星運行的星體，月球是地球的衛星。"},
        {"question": "太陽系中唯一能自行發光和發熱的星體是什麼？", "options": ["地球", "木星", "太陽", "月球"], "answer": "太陽", "explanation": "太陽是一顆恆星，能夠通過內部的核聚變反應產生光和熱。"},
        {"question": "太陽系位於宇宙中哪個星系之內？", "options": ["仙女座星系", "三角座星系", "銀河系", "大小麥哲倫星系"], "answer": "銀河系", "explanation": "我們的太陽系是銀河系中數千億個恆星系之一。"},
        {"question": "按照與太陽的距離，由近至遠排列，地球排在第幾位？", "options": ["第一位", "第二位", "第三位", "第四位"], "answer": "第三位", "explanation": "八大行星由近至遠的次序是：水星、金星、地球、火星、木星、土星、天王星、海王星。"},
        {"question": "哪個行星因為表面富含氧化鐵而呈現橙紅色？", "options": ["金星", "地球", "火星", "木星"], "answer": "火星", "explanation": "火星的表面土壤和岩石富含氧化鐵（鐵鏽），因此呈現標誌性的橙紅色。"},
        {"question": "首位登陸月球的太空人是哪國人？", "options": ["前蘇聯人", "中國人", "美國人", "法國人"], "answer": "美國人", "explanation": "1969年，美國太空人岩士唐（Neil Armstrong）成為第一位踏上月球的人類。"},
        {"question": "中國首位進入太空的太空人是誰？", "options": ["聶海勝", "楊利偉", "翟志剛", "王亞平"], "answer": "楊利偉", "explanation": "2003年，楊利偉乘坐「神舟五號」飛船進入太空，成為中國首位太空人。"},
        {"question": "汽車司機用來確定位置和尋找路線的技術，主要依賴哪種衛星？", "options": ["氣象衛星", "通訊衛星", "遙感衛星", "導航衛星"], "answer": "導航衛星", "explanation": "導航衛星（如GPS系統）提供精確的定位和時間信息，用於導航。"},
        {"question": "電視台直播海外節目時，需要利用哪種衛星轉發信號？", "options": ["氣象衛星", "通訊衛星", "遙感衛星", "導航衛星"], "answer": "通訊衛星", "explanation": "通訊衛星在太空中接收地面站發來的信號，並將其放大、轉發到另一個地面站，實現遠距離通訊。"},
        {"question": "天氣預報中使用的雲圖，是由哪種衛星提供的？", "options": ["氣象衛星", "通訊衛星", "遙感衛星", "導航衛星"], "answer": "氣象衛星", "explanation": "氣象衛星從太空監測雲層、溫度等天氣數據，幫助預測天氣。"},
        {"question": "世界首位進入太空的人是誰？", "options": ["岩士唐", "楊利偉", "加加林", "王亞平"], "answer": "加加林", "explanation": "1961年，前蘇聯太空人加加林乘坐「東方一號」進入太空，成為首位進入太空的人類。"},
        # ... (Add 60 more GS questions here to reach 80)
    ] * 4 # Duplicate to reach 80 questions
    return random.sample(question_bank, num_questions)


# --- Streamlit Web App Logic ---

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'subject' not in st.session_state:
    st.session_state.subject = ''

subjects = {
    "中文": generate_chinese_questions, 
    "英文": generate_english_questions,
    "數學": generate_maths_questions, 
    "常識": generate_gs_questions
}

def start_quiz(subject_name):
    st.session_state.subject = subject_name
    st.session_state.quiz_questions = subjects[subject_name](20)
    st.session_state.user_answers = []
    st.session_state.current_question = 0
    st.session_state.page = 'quiz'

def display_start_page():
    st.title("小五溫習程式")
    st.header("請選擇要練習的科目")

    for subject in subjects:
        if st.button(subject, key=subject, use_container_width=True):
            start_quiz(subject)
            st.rerun()

def display_quiz_page():
    st.title(f"科目：{st.session_state.subject}")
    
    idx = st.session_state.current_question
    q_data = st.session_state.quiz_questions[idx]
    
    st.subheader(f"第 {idx + 1} / 20 題")
    st.write(q_data['question'])

    with st.form(key=f"q_{idx}"):
        if 'options' in q_data:
            user_answer = st.radio("請選擇答案：", q_data['options'], index=None, key=f"radio_{idx}")
        else:
            user_answer = st.text_input("請輸入答案：", key=f"text_{idx}")
        
        submitted = st.form_submit_button("提交答案")
        if submitted:
            st.session_state.user_answers.append(user_answer)
            if st.session_state.current_question < 19:
                st.session_state.current_question += 1
            else:
                st.session_state.page = 'results'
            st.rerun()

def display_results_page():
    st.title("測驗結果")
    
    score = 0
    for i, q_data in enumerate(st.session_state.quiz_questions):
        user_ans = st.session_state.user_answers[i] if i < len(st.session_state.user_answers) else "未作答"
        correct_ans = q_data['answer']
        is_correct = (str(user_ans) == str(correct_ans))
        if is_correct:
            score += 1

        with st.container(border=True):
            st.subheader(f"第 {i+1} 題：{q_data['question']}")
            if is_correct:
                st.success(f"你的答案：{user_ans} (正確 ✓)")
            else:
                st.error(f"你的答案：{user_ans} (錯誤 ✗)")
                st.info(f"正確答案：{correct_ans}")
            
            if 'explanation' in q_data:
                st.markdown(f"**詳解：** {q_data['explanation']}")

    st.header(f"總分：{score} / 20")

    if st.button("返回主選單", use_container_width=True):
        # Reset all state variables for a clean start
        st.session_state.page = 'start'
        st.session_state.quiz_questions = []
        st.session_state.user_answers = []
        st.session_state.current_question = 0
        st.session_state.subject = ''
        st.rerun()

# Main app router
if st.session_state.page == 'start':
    display_start_page()
elif st.session_state.page == 'quiz':
    display_quiz_page()
elif st.session_state.page == 'results':
    display_results_page()
