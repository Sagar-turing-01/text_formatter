import streamlit as st
import re

def transform(text: str) -> str:
    """
    1. Turn the two-character sequence '\\n' into a real newline.
    2. Split the text into lines.
    3. Bold 'Step X:' lines, indent everything else.
    4. Join with '  \\n' (two spaces + newline) so Markdown keeps breaks.
    """
    text = text.replace("\\n", "\n")              # ① literal -> real newline

    out_lines = []
    step_counter = 1
    new_text = """"""
    for line in text.splitlines():
        stripped = line.strip()

        # Detect either '## ' markdown heading or an existing 'Step X:' prefix
        if stripped.startswith("##"):
            header = stripped.lstrip("#").strip()
            out_lines.append(f"**Step {step_counter}: {header}**")
            step_counter += 1
            new_text += " \n" + out_lines[-1]

        elif re.match(r"(?i)^step\s+\d+\s*:", stripped):
            out_lines.append(f"**{stripped}**")    # already a Step line
            new_text += " \n" + out_lines[-1]
        else:
            s_text = "    " + stripped
            out_lines.append(s_text)    # simple indent
            new_text += "     \n    " + out_lines[-1]
    # Markdown line-break = two spaces + newline
    return new_text


# ────────── Streamlit UI ──────────
st.title("Steps Formatter")

sample = (
    ""
)

user_text = st.text_area("Paste your text here",
                         value=sample, height=300)

if st.button("Transform"):
    st.markdown(transform(user_text))
