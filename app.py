import html

import requests
import streamlit as st

# =========================
# Config
# =========================
API_URL = "https://hypertext-rinse-reapply.ngrok-free.dev/recommend"

try:
    API_KEY = st.secrets["API_KEY"]
except Exception:
    API_KEY = "easyone123"

st.set_page_config(
    page_title="Art Sense",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================
# Custom CSS
# =========================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
}

/* Hide default Streamlit chrome + sidebar */
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
section[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] { display: none !important; }

.stApp {
    background:
        radial-gradient(circle at 15% 0%, rgba(229, 9, 20, 0.14) 0%, transparent 40%),
        radial-gradient(circle at 85% 100%, rgba(99, 102, 241, 0.14) 0%, transparent 40%),
        #0b0d14;
}

.block-container { max-width: 760px; padding-top: 2.5rem; }

/* Hero */
.hero { text-align: center; margin-bottom: 2rem; }
.eyebrow {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #ff6b6b;
    background: rgba(255, 107, 107, 0.1);
    border: 1px solid rgba(255, 107, 107, 0.25);
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    margin-bottom: 1rem;
}
.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin: 0 0 0.8rem;
    color: #ffffff;
}
.hero h1 span {
    background: linear-gradient(90deg, #ff4b5c, #ff9a5a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    color: #9aa0b4;
    font-size: 1.05rem;
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Section labels */
.section-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c829a;
    margin: 1.4rem 0 0.5rem;
}

/* Text input */
.stTextInput input {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 14px !important;
    color: #f1f2f7 !important;
    font-size: 1rem !important;
    padding: 1rem !important;
}
.stTextInput input:focus {
    border-color: #ff4b5c !important;
    box-shadow: 0 0 0 3px rgba(255, 75, 92, 0.2) !important;
}

/* Hide "Press Enter to submit form" hint */
div[data-testid="InputInstructions"] { display: none !important; }

/* Example buttons */
div.stButton > button {
    width: 100%;
    background: rgba(255, 255, 255, 0.05);
    color: #d7daea;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 0.55rem;
    font-weight: 500;
    transition: all 0.2s ease;
}
div.stButton > button:hover {
    border-color: #ff4b5c;
    color: #ffffff;
    background: rgba(255, 75, 92, 0.1);
}

/* Main submit button (inside form) */
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(90deg, #e50914, #ff5a36);
    color: #ffffff;
    border: none;
    padding: 0.8rem;
    font-size: 1.05rem;
    font-weight: 700;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(229, 9, 20, 0.3);
    transition: all 0.2s ease;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
    color: #ffffff;
}

/* Results */
.results-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    margin: 2.2rem 0 1rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.results-header h2 { color: #fff; font-size: 1.4rem; font-weight: 700; margin: 0; }
.results-header span { color: #7c829a; font-size: 0.9rem; }

/* Movie card = <details> (click to expand) */
details.movie-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    margin-bottom: 0.9rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
details.movie-card:hover {
    border-color: rgba(255, 75, 92, 0.5);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
}
details.movie-card[open] { border-color: rgba(255, 75, 92, 0.5); }

details.movie-card > summary {
    display: flex;
    align-items: flex-start;
    gap: 1.1rem;
    padding: 1.2rem 1.4rem;
    cursor: pointer;
    list-style: none;
    user-select: none;
}
details.movie-card > summary::-webkit-details-marker { display: none; }
details.movie-card > summary::marker { content: ""; }

.rank {
    flex-shrink: 0;
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(135deg, #e50914, #ff7a45);
    color: #fff;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
}
.movie-body { flex: 1; min-width: 0; }
.movie-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.8rem;
}
.movie-title { color: #ffffff; font-size: 1.15rem; font-weight: 700; }
.match-badge {
    flex-shrink: 0;
    font-size: 0.8rem;
    font-weight: 700;
    color: #ffb199;
    background: rgba(255, 107, 107, 0.12);
    border: 1px solid rgba(255, 107, 107, 0.3);
    padding: 0.2rem 0.65rem;
    border-radius: 999px;
}
.match-bar {
    height: 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 999px;
    overflow: hidden;
    margin: 0.6rem 0 0.5rem;
}
.match-bar > div {
    height: 100%;
    background: linear-gradient(90deg, #e50914, #ff9a5a);
    border-radius: 999px;
}
.movie-hint { color: #7c829a; font-size: 0.78rem; }
.chev {
    flex-shrink: 0;
    color: #7c829a;
    font-size: 1rem;
    line-height: 40px;
    transition: transform 0.2s ease;
}
details.movie-card[open] .chev { transform: rotate(180deg); }
details.movie-card[open] .movie-hint { display: none; }

.movie-details {
    padding: 0 1.4rem 1.3rem 4.1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    margin-top: -0.2rem;
}
.movie-genres { color: #ff8f8f; font-size: 0.8rem; font-weight: 600; margin: 0.9rem 0 0.3rem; }
.movie-label {
    color: #7c829a;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin: 0.8rem 0 0.2rem;
}
.movie-overview { color: #c4c9db; font-size: 0.92rem; line-height: 1.65; }
.movie-exp { color: #aab0c4; font-size: 0.92rem; line-height: 1.65; }

/* Footer */
.app-footer {
    text-align: center;
    color: #5d637a;
    font-size: 0.82rem;
    margin-top: 3rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# Hero
# =========================
st.markdown(
    """
<div class="hero">
    <div class="eyebrow">AI-Powered Discovery</div>
    <h1>Find your next <span>favorite movie</span></h1>
    <p>Describe a story, a mood, or a concept, and we'll recommend
    movies that match your idea.</p>
</div>
""",
    unsafe_allow_html=True,
)

# =========================
# Example ideas
# =========================
EXAMPLES = {
    "👻 Horror": "A group of friends trapped in an abandoned place where something dangerous is hunting them.",
    "🚀 Sci-Fi": "An astronaut stranded on a distant planet must find a way to survive and return home.",
    "🕵️ Crime": "A detective hunts a serial killer who leaves clues connected to old fairy tales.",
}

if "idea" not in st.session_state:
    st.session_state.idea = ""

st.markdown('<div class="section-label">Quick examples</div>', unsafe_allow_html=True)
cols = st.columns(len(EXAMPLES))
for col, (label, text) in zip(cols, EXAMPLES.items()):
    if col.button(label, key=f"example_{label}"):
        st.session_state.idea = text

# =========================
# Input form (Enter submits)
# =========================
st.markdown('<div class="section-label">Your movie idea</div>', unsafe_allow_html=True)

with st.form("idea_form", border=False):
    user_idea = st.text_input(
        "Your movie idea",
        key="idea",
        placeholder="e.g. A group of friends trapped in an abandoned place where something dangerous is hunting them...",
        label_visibility="collapsed",
    )
    submit = st.form_submit_button(
        "Get Recommendations", type="primary", use_container_width=True
    )


# =========================
# Helpers
# =========================
def render_movie_card(rank: int, movie: dict) -> str:
    """Build one expandable movie card as a single-line HTML string
    (no blank lines, so Streamlit's markdown parser doesn't break it)."""
    title = html.escape(str(movie.get("title", "Untitled")))
    explanation = html.escape(str(movie.get("explanation", "") or ""))
    overview = html.escape(str(movie.get("overview", "") or ""))
    genres = html.escape(str(movie.get("genres", "") or ""))

    try:
        similarity = max(0.0, min(100.0, float(movie.get("similarity", 0))))
    except (TypeError, ValueError):
        similarity = 0.0

    parts = [
        '<details class="movie-card">',
        "<summary>",
        f'<div class="rank">{rank}</div>',
        '<div class="movie-body">',
        '<div class="movie-top">',
        f'<div class="movie-title">{title}</div>',
        f'<div class="match-badge">{similarity:.0f}% match</div>',
        "</div>",
        f'<div class="match-bar"><div style="width:{similarity}%"></div></div>',
        '<div class="movie-hint">Click to see the description</div>',
        "</div>",
        '<div class="chev">&#9662;</div>',
        "</summary>",
        '<div class="movie-details">',
    ]
    if genres:
        parts.append(f'<div class="movie-genres">{genres}</div>')
    parts.append(
        '<div class="movie-label">Description</div>'
        f'<div class="movie-overview">{overview or "No description available."}</div>'
    )
    if explanation:
        parts.append(
            '<div class="movie-label">Why it matches</div>'
            f'<div class="movie-exp">{explanation}</div>'
        )
    parts.append("</div></details>")
    return "".join(parts)


# =========================
# Action
# =========================
if submit:
    if not user_idea.strip():
        st.warning("Please describe your movie idea first.")
    else:
        with st.spinner("Analyzing your idea and finding the best matches..."):
            try:
                response = requests.post(
                    API_URL,
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "ngrok-skip-browser-warning": "true",
                    },
                    json={"idea": user_idea},
                    timeout=120,
                )

                if response.status_code == 200:
                    recommendations = response.json().get("recommendations", [])

                    if not recommendations:
                        st.info(
                            "No recommendations found. Try adding more detail to your idea."
                        )
                    else:
                        st.markdown(
                            f"""
                            <div class="results-header">
                                <h2>Recommended for you</h2>
                                <span>{len(recommendations)} matches</span>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                        for i, movie in enumerate(recommendations, start=1):
                            st.markdown(
                                render_movie_card(i, movie),
                                unsafe_allow_html=True,
                            )
                else:
                    st.error(f"The service returned an error (HTTP {response.status_code}).")
                    with st.expander("Error details"):
                        st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error(
                    "Could not connect to the recommendation service. "
                    "Please check that the API is running and try again."
                )
                with st.expander("Error details"):
                    st.code(str(e))

# =========================
# Footer
# =========================
st.markdown(
    '<div class="app-footer">Art Sense · Powered by AI recommendations</div>',
    unsafe_allow_html=True,
)
