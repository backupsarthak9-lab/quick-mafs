import streamlit as st
import random

# ==================== CUTE MESSAGES ====================

CORRECT_MESSAGES = [
    "Perfect. Clean reasoning, clean answer.",
    "That was sharp — you didn't hesitate.",
    "Exactly right. Nice thinking.",
    "You handled that beautifully.",
    "That was confident and precise.",
    "Correct — and you made it look easy.",
    "Great instincts there.",
    "That's the kind of clarity that compounds.",
    "Nicely done. Very controlled.",
    "You're thinking really clearly today.",
    "That was solid reasoning.",
    "Correct. No objections.",
    "That felt effortless, didn't it?",
    "You trusted your thinking — and it paid off.",
    "Exactly right. Proud of you.",
    "That was smooth.",
    "You're in a good rhythm today.",
    "That's a win.",
    "Clean answer, no noise.",
    "You're really good at this.",
    "That focus is showing.",
    "Correct — and well-earned.",
    "You're sharper than you give yourself credit for.",
    "That was decisive.",
    "Nicely argued 😉",
]

WRONG_MESSAGES = [
    "Close — walk through it once more.",
    "Not quite, but your approach makes sense.",
    "Almost there. Take a breath and try again.",
    "You're thinking in the right direction.",
    "That was a good attempt — refine it slightly.",
    "Pause for a second and recheck.",
    "You're closer than you think.",
    "Try once more, no rush.",
    "That's okay — learning happens here.",
    "You didn't miss by much.",
    "Good reasoning, just adjust it.",
    "Take another look — you've got this.",
    "It'll click. Give it another go.",
    "That was thoughtful — now tighten it up.",
    "No pressure. Try again.",
    "You're doing fine. One more pass.",
    "This one needs a little patience.",
    "Almost. Trust your process.",
    "That's part of getting sharper.",
    "You're not wrong — just not finished yet.",
    "Slow it down and revisit.",
    "This is the good kind of challenge.",
    "You're learning even here.",
    "Keep going. I believe in you.",
    "Try again — I know you can get it.",
]

RARE_MESSAGES = [
    "Watching you think like this is my favorite part.",
    "Proud of you for showing up today.",
    "You're doing more than you realize.",
    "Quiet progress is still progress.",
]

# ==================== LOVE MESSAGES ====================

LOVE_MESSAGES = [
    "you make my days better without even trying",
    "thinking about you always makes me feel calmer",
    "you’re honestly so smart it surprises me sometimes",
    "you’re going to be a really good lawyer one day, like actually",
    "i like how you notice things most people miss",
    "the way your brain works is really impressive",
    "you’re so thoughtful in every way",
    "you’re smart and kind, which is such a rare combo",
    "you handle things with so much maturity, it’s really admirable",
    "you make hard days feel a lot easier for me",
    "you care so deeply and it shows in everything you do",
    "you’re really observant, in the best way",
    "i like how seriously you take learning and growing",
    "you think so clearly, even when things get stressful",
    "you’re going to be such a strong advocate someday",
    "you have really good instincts, trust them",
    "being around you just feels grounding in a good way",
    "you make effort look effortless even when i know it’s not",
    "you’re genuinely one of the smartest people i know",
    "you’re so good at understanding people and situations",
    "you have such a calm confidence about you",
    "you’re doing really well, even on days it doesn’t feel like it",
    "i like how you’re always trying to be better",
    "you make me feel proud just by being you",
    "you’re really good at thinking things through",
    "you’re going to do amazing things in law, i believe that",
    "you’re thoughtful in a way that feels very you",
    "you make the world feel a little less overwhelming",
    "you’re so capable and you don’t even realize it sometimes",
    "i really admire how seriously you take your work",
    "you’re building something meaningful for yourself",
    "you’re smart in a quiet, confident way",
    "you make my day better every time you cross my mind",
    "you’re really good at seeing the bigger picture",
    "you have such a good balance of logic and empathy",
    "you’re going to be an incredible lawyer, but an even better person",
    "i really like how deeply you think about things",
    "you’re doing enough, even when it feels like you’re not",
    "you make everything feel kind of beautiful",
    "you’re really special, just saying",
    "i’m really glad i get to know you",
    "aap bohot pyaare ho",
    "mujhe aap se baat karna bohot accha lagta hai"
    "you make me feel lucky",
]

# ==================== PHASE 1: CORE LOGIC ====================

def get_correct_message():
    """
    Get a correct answer message. 20% chance of rare message.
    """
    if random.random() < 0.2:  # 20% chance for rare message
        return random.choice(RARE_MESSAGES)
    return random.choice(CORRECT_MESSAGES)


def generate_daily_problems():
    """
    Generate 3 daily math problems using current timestamp as seed.
    Returns list of {question, answer} dicts.
    """
    # Use current timestamp as seed for fresh problems on each refresh
    import time
    seed = int(time.time())
    random.seed(seed)

    problems = []

    for i in range(3):
        operation = random.choice(['add', 'subtract', 'multiply', 'divide'])

        if operation == 'add':
            a = random.randint(50, 200)
            b = random.randint(50, 200)
            question = f"{a} + {b}"
            answer = a + b

        elif operation == 'subtract':
            a = random.randint(100, 500)
            b = random.randint(50, a)
            question = f"{a} - {b}"
            answer = a - b

        elif operation == 'multiply':
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            question = f"{a} × {b}"
            answer = a * b

        elif operation == 'divide':
            # Clean division - generate answer first then multiply
            answer = random.randint(2, 15)
            divisor = random.randint(2, 10)
            dividend = answer * divisor
            question = f"{dividend} ÷ {divisor}"

        problems.append({
            'question': question,
            'answer': answer
        })

    return problems


# ==================== PHASE 2: INTERACTIVE UI ====================

def load_custom_css():
    """Load custom dark purple minimalistic theme"""
    css = """
    <style>
    /* Import SF Pro-like font */
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');

    /* Pink purple background */
    .stApp {
        background: #0f0a12 !important;
        background-image:
            radial-gradient(at 0% 0%, rgba(217, 70, 239, 0.25) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.2) 0px, transparent 50%) !important;
        font-family: 'SF Pro Display', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #f5e6f3 !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* Title - clean and natural */
    h1 {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 500 !important;
        text-align: center !important;
        font-size: 2rem !important;
        margin-bottom: 2rem !important;
        letter-spacing: -0.02em !important;
        opacity: 1 !important;
        background: none !important;
        -webkit-background-clip: unset !important;
        -webkit-text-fill-color: unset !important;
        background-clip: unset !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
    }

    /* Container - centered and spacious */
    .block-container {
        padding: 4rem 2rem !important;
        max-width: 700px !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        min-height: 100vh !important;
    }

    /* Question - clean and readable */
    h3 {
        color: #ffffff !important;
        font-weight: 300 !important;
        font-size: 4rem !important;
        text-align: center !important;
        padding: 1rem 0 !important;
        background: transparent !important;
        border: none !important;
        margin: 1rem 0 2rem 0 !important;
        letter-spacing: -0.02em !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
    }

    /* Progress text - subtle */
    p, .stMarkdown {
        color: rgba(255, 255, 255, 0.5) !important;
        font-weight: 400 !important;
        font-size: 0.95rem !important;
        text-align: center !important;
        letter-spacing: -0.01em !important;
        margin-bottom: 1.5rem !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
    }

    strong {
        color: rgba(255, 255, 255, 0.85) !important;
        font-weight: 500 !important;
    }

    /* Input field - SUPER WIDE, fully transparent, centered text */
    div[data-testid="stNumberInput"] input,
    .stNumberInput input,
    input[type="number"] {
        background: transparent !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 14px !important;
        padding: 1.5rem 6rem !important;
        font-size: 2.2rem !important;
        text-align: center !important;
        font-weight: 300 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
        color: #ffffff !important;
        transition: all 0.15s ease !important;
        letter-spacing: 0em !important;
        width: 100% !important;
        max-width: 90% !important;
        margin: 0 auto !important;
        display: block !important;
        backdrop-filter: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stNumberInput"] input:focus,
    .stNumberInput input:focus,
    input[type="number"]:focus {
        border-color: rgba(255, 255, 255, 0.1) !important;
        background: transparent !important;
        box-shadow: none !important;
        outline: none !important;
        transform: none !important;
    }

    div[data-testid="stNumberInput"] input::placeholder,
    .stNumberInput input::placeholder,
    input[type="number"]::placeholder {
        color: rgba(255, 255, 255, 0.28) !important;
        font-weight: 300 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
        text-align: center !important;
    }

    /* Hide label */
    div[data-testid="stNumberInput"] label,
    .stNumberInput label {
        display: none !important;
    }

    /* Center the input container */
    div[data-testid="stNumberInput"],
    .stNumberInput {
        display: flex !important;
        justify-content: center !important;
    }

    div[data-testid="stNumberInput"] > div,
    .stNumberInput > div {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }

    /* HIDE Submit button - Enter key only */
    div[data-testid="stFormSubmitButton"],
    .stFormSubmitButton {
        display: none !important;
        visibility: hidden !important;
    }

    /* ALL other buttons - clean universal style */
    div[data-baseweb="button"],
    .stButton button,
    button:not([kind="primaryFormSubmit"]) {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        padding: 0.9rem 1.8rem !important;
        font-weight: 400 !important;
        font-size: 0.95rem !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
        transition: all 0.15s ease !important;
        width: 100% !important;
        backdrop-filter: none !important;
        letter-spacing: 0em !important;
        min-height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1.3 !important;
        box-shadow: none !important;
        cursor: pointer !important;
    }

    div[data-baseweb="button"]:hover,
    .stButton button:hover,
    button:not([kind="primaryFormSubmit"]):hover {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: rgba(255, 255, 255, 0.18) !important;
        color: rgba(255, 255, 255, 0.9) !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* Success message */
    div[data-testid="stSuccess"],
    .stSuccess {
        background: rgba(16, 185, 129, 0.15) !important;
        color: #86efac !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 2px solid rgba(16, 185, 129, 0.4) !important;
        font-weight: 500 !important;
        font-size: 1.15rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
        text-align: center !important;
    }

    /* Error message */
    div[data-testid="stError"],
    .stError {
        background: rgba(239, 68, 68, 0.15) !important;
        color: #fca5a5 !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 2px solid rgba(239, 68, 68, 0.4) !important;
        font-weight: 500 !important;
        font-size: 1.15rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
        text-align: center !important;
    }

    /* Warning message */
    div[data-testid="stWarning"],
    .stWarning {
        background: rgba(245, 158, 11, 0.15) !important;
        color: #fcd34d !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 2px solid rgba(245, 158, 11, 0.4) !important;
        font-weight: 500 !important;
        font-size: 1.15rem !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
        text-align: center !important;
    }

    /* Fade in animation */
    .element-container {
        animation: fadeIn 0.6s ease-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Form spacing */
    div[data-testid="stForm"],
    .stForm {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }

    /* Remove spinners from number input */
    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none !important;
        margin: 0 !important;
        display: none !important;
    }
    input[type=number] {
        -moz-appearance: textfield !important;
    }

    /* Hide the step buttons */
    div[data-testid="stNumberInput"] button,
    .stNumberInput button {
        display: none !important;
        visibility: hidden !important;
    }

    /* Hide step button container */
    div[data-testid="stNumberInput"] div[role="button"],
    .stNumberInput div[role="button"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* Purple hearts animation */
    @keyframes floatHeart {
        0% {
            transform: translateY(0) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) scale(1.5);
            opacity: 0;
        }
    }

    .heart {
        position: fixed !important;
        font-size: 3.5rem !important;
        animation: floatHeart 3s ease-in-out forwards !important;
        pointer-events: none !important;
        z-index: 9999 !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display: none;}
        div[data-testid="stDecoration"] {display: none;}
        div[data-testid="stFooter"] {display: none;}
        </style>
        """, unsafe_allow_html=True)


def show_purple_hearts():
    """Display purple hearts animation"""
    import random
    hearts_html = ""
    for i in range(12):
        left = random.randint(10, 90)
        delay = random.uniform(0, 0.8)
        hearts_html += f"""
        <div class="heart" style="left: {left}%; bottom: 0; animation-delay: {delay}s;">
            💜
        </div>
        """
    st.markdown(hearts_html, unsafe_allow_html=True)


def load_love_page_css():
    """Load clean love page theme"""
    css = """
    <style>
    .stApp {
        background: #0f0a12 !important;
        background-image:
            radial-gradient(at 0% 0%, rgba(217, 70, 239, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.1) 0px, transparent 50%) !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
        color: #ffffff !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* Container - centered */
    .block-container {
        padding: 4rem 2rem !important;
        max-width: 700px !important;
        margin: 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        min-height: 100vh !important;
    }

    /* Buttons on love page - clean style */
    div[data-baseweb="button"],
    .stButton button,
    button {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 400 !important;
        font-size: 3.5rem !important;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif !important;
        transition: all 0.15s ease !important;
        width: 100% !important;
        backdrop-filter: none !important;
        letter-spacing: 0em !important;
        min-height: 100px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1 !important;
        box-shadow: none !important;
    }

    div[data-baseweb="button"]:hover,
    .stButton button:hover,
    button:hover {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: rgba(255, 255, 255, 0.18) !important;
        color: rgba(255, 255, 255, 0.9) !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* Back button - smaller text */
    button:contains("Back") {
        font-size: 0.95rem !important;
        min-height: 44px !important;
        padding: 0.75rem 1.5rem !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def show_love_page():
    """Display the love message page"""
    load_love_page_css()

    # Initialize message index
    if 'current_love_message' not in st.session_state:
        st.session_state.current_love_message = random.choice(LOVE_MESSAGES)

    # Display message big and centered
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"<h1 style='text-align: center; font-size: 2.5rem; color: #ffffff; font-weight: 400; margin: 6rem 2rem 4rem 2rem; line-height: 1.6;'>{st.session_state.current_love_message}</h1>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # Sloth button - using image if exists, otherwise emoji
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # Try to use image first, fallback to emoji
        import os
        sloth_path = "sloth.png"  # You can upload your sloth image here
        if os.path.exists(sloth_path):
            # Display image button
            if st.button("", key="another_message", use_container_width=True):
                st.session_state.current_love_message = random.choice(LOVE_MESSAGES)
                st.rerun()
            st.markdown(f"<div style='text-align: center; margin-top: -80px;'><img src='data:image/png;base64,{{}}' style='width: 120px; height: 120px; pointer-events: none;'></div>", unsafe_allow_html=True)
        else:
            # Fallback to emoji - make it REALLY big
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            if st.button("🦥", key="another_message", use_container_width=True):
                st.session_state.current_love_message = random.choice(LOVE_MESSAGES)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)


def main():
    # Check if we should show the love page
    if 'show_love_page' in st.session_state and st.session_state.show_love_page:
        show_love_page()
        return

    load_custom_css()
    st.title("Dori Math 🐟🦄")

    # Initialize session state
    if 'problems' not in st.session_state:
        st.session_state.problems = generate_daily_problems()
        st.session_state.current_problem = 0
        st.session_state.completed = False
        st.session_state.feedback_message = None
        st.session_state.feedback_type = None

    problems = st.session_state.problems
    current = st.session_state.current_problem

    # Clear feedback when moving to new problem (but preserve if we just showed hearts)
    if 'last_problem' not in st.session_state:
        st.session_state.last_problem = current
    elif st.session_state.last_problem != current:
        # Only clear if we're not showing hearts
        if not st.session_state.get('show_hearts_now', False):
            st.session_state.feedback_message = None
            st.session_state.feedback_type = None
        st.session_state.last_problem = current
        st.session_state.show_hearts_now = False

    # Check if all problems are completed
    if current >= len(problems):
        st.session_state.completed = True

    # Show completion message
    if st.session_state.completed:
        st.success("🤍 Amazing! You completed all 3 problems! So proud of you!")
        st.balloons()
        st.write("")

        # Two buttons side by side
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✨ we go again twin", use_container_width=True):
                st.session_state.problems = generate_daily_problems()
                st.session_state.current_problem = 0
                st.session_state.completed = False
                st.rerun()
        with col2:
            if st.button("hehehe 🦥", use_container_width=True, key="sloth_button"):
                st.session_state.show_love_page = True
                st.rerun()
        return

    # Display current problem
    problem = problems[current]
    st.write(f"**Problem {current + 1} of {len(problems)}**")
    st.write("")
    st.write(f"### {problem['question']}")
    st.write("")

    # Display feedback message if exists (with Baymax!)
    if st.session_state.feedback_message:
        baymax = "🤍"  # Baymax placeholder - you can replace with image later
        if st.session_state.feedback_type == "success":
            st.success(f"{baymax} {st.session_state.feedback_message}")
            show_purple_hearts()  # Show hearts animation on correct answer
        elif st.session_state.feedback_type == "error":
            st.error(f"{baymax} {st.session_state.feedback_message}")
        elif st.session_state.feedback_type == "warning":
            st.warning(f"{baymax} {st.session_state.feedback_message}")

    # Form for Enter key submission
    with st.form(key=f"answer_form_{current}"):
        user_answer = st.number_input(
            "Answer",
            value=None,
            step=1,
            format="%d",
            key=f"answer_{current}",
            placeholder="Type your answer...",
            label_visibility="collapsed"
        )

        submitted = st.form_submit_button("Submit", type="primary")

        if submitted:
            if user_answer is None:
                st.session_state.feedback_message = "Please enter an answer!"
                st.session_state.feedback_type = "warning"
                st.rerun()
            elif user_answer == problem['answer']:
                st.session_state.feedback_message = get_correct_message()
                st.session_state.feedback_type = "success"
                st.session_state.show_hearts_now = True  # Flag to show hearts
                st.session_state.current_problem += 1
                st.rerun()
            else:
                st.session_state.feedback_message = random.choice(WRONG_MESSAGES)
                st.session_state.feedback_type = "error"
                st.rerun()


if __name__ == "__main__":
    main()
