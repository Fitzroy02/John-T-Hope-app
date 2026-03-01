# Pricing & points architecture: £10 ceiling, £7–£8 target, Option 1 points system
import streamlit as st

st.set_page_config(page_title="Lumen – Pricing & Points Architecture", layout="wide")

st.title("🎵🎬 Lumen: Pricing & Points Architecture")
st.write(
    "You're setting three anchors at once — **Option 1 for points**, **£10 as a hard ceiling**, "
    "and **£7–£8 as the strategic target** — and Lumen is absolutely coherent within that structure. "
    "What you're doing is building a *low‑price, high‑ethics, high‑value* model that can undercut "
    "the market without collapsing margin."
)

st.divider()

# ── Streaming Price Architecture ─────────────────────────────────────────────
st.header("🎧 Streaming Price Architecture with a £10 Ceiling and £7–£8 Target")

st.write("Your position is now:")
st.markdown(
    "- **£10 = absolute maximum retail price**\n"
    "- **£7–£8 = preferred operating price**\n"
    "- **Aim: be cheaper than the lowest music + film streamer in the UK market**"
)
st.write("This creates a three‑tier logic:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Hard Ceiling (non‑negotiable)")
    st.metric(label="Maximum Price", value="£10")
    st.write(
        "No user ever pays more than **£10**. "
        "This becomes your ethical and competitive identity."
    )

with col2:
    st.subheader("2. Target Retail Price")
    st.metric(label="Target Range", value="£7–£8")
    st.write("This is only possible if:")
    st.markdown(
        "- AIM licensing is reduced\n"
        "- You gain economies of scale\n"
        "- Posting fees and family bundles offset some cost"
    )

with col3:
    st.subheader("3. Strategic Undercutting")
    st.write("To be cheaper than the lowest competitor, you need:")
    st.markdown(
        "- A **volume‑based licensing deal** with AIM\n"
        "- A **dual‑service bundle** that beats Spotify + Netflix + Amazon + Apple\n"
        "- A **family structure** that keeps ARPU stable even at low prices"
    )

st.divider()

# ── Points System ─────────────────────────────────────────────────────────────
st.header("📊 Option 1 Confirmed: 50 Thumbs‑Up per Month at 20 Points Each")

st.write("Your choice stabilises the maths cleanly:")

pts_col1, pts_col2, pts_col3, pts_col4, pts_col5 = st.columns(5)
pts_col1.metric("Points per thumbs‑up", "20")
pts_col2.metric("Thumbs‑up per month", "50")
pts_col3.metric("Points per member", "1,000")
pts_col4.metric("Points per team", "4,000")
pts_col5.metric("Max members per family", "2")

st.write("This keeps the system **fair, predictable, and resistant to gaming**.")
st.caption("Note: a *team* can have up to 4 members; a *family* subscription caps at 2 members per account.")

st.divider()

# ── How Pricing and Points Reinforce Each Other ───────────────────────────────
st.header("🧩 How the Pricing and Points System Reinforce Each Other")
st.write(
    "The two systems now support the same strategic goal: "
    "**low price, high engagement, ethical governance.**"
)

left, right = st.columns(2)

with left:
    st.subheader("Pricing supports:")
    st.markdown(
        "- Market competitiveness\n"
        "- Family affordability\n"
        "- AIM negotiation leverage\n"
        "- Predictable revenue"
    )

with right:
    st.subheader("Points system supports:")
    st.markdown(
        "- Community growth\n"
        "- Organic subscriber acquisition\n"
        "- Creative contribution\n"
        "- Fair representation (family cap)"
    )

st.write(
    "Together, they create a **self‑funding ecosystem** where:"
)
st.markdown(
    "- Low subscription prices attract users\n"
    "- Posting fees and family bundles stabilise revenue\n"
    "- Points‑driven referrals reduce marketing spend\n"
    "- AIM licensing becomes cheaper as volume grows\n"
    "- Lower licensing cost allows you to drop prices further\n"
    "- Lower prices attract more users — **and the cycle repeats**"
)
st.info(
    "This is the same flywheel used by the most successful digital platforms — "
    "but with your ethical framing and governance."
)

st.divider()

# ── AIM Negotiation ───────────────────────────────────────────────────────────
st.header("💷 What the AIM Negotiation Now Looks Like")
st.write("You can now go to AIM with a clear, mathematically grounded position:")
st.info(
    '"Our maximum retail price is £10, but our target is £7–£8. '
    "To achieve this, we need a licensing structure that scales with volume. "
    "If AIM supports us, we can become the lowest‑priced dual‑streaming service in the UK, "
    'which increases volume for both sides."'
)

st.write("Your leverage points:")
st.markdown(
    "- You're not asking for a discount to increase profit — you're asking to **lower the user price**.\n"
    "- You're building a **community‑driven, ethically governed platform**, which aligns with AIM's mission.\n"
    "- You can demonstrate **predictable subscriber growth** through the points system.\n"
    "- You can show **posting revenue** as an additional stabiliser."
)
st.success("This is a strong negotiation position.")

st.divider()

# ── Clean Integrated Model ────────────────────────────────────────────────────
st.header("📐 Clean Integrated Model (Current State)")

model_col1, model_col2, model_col3 = st.columns(3)

with model_col1:
    st.subheader("Subscription")
    st.markdown(
        "| Item | Value |\n"
        "| --- | --- |\n"
        "| Hard ceiling | £10 |\n"
        "| Target price | £7–£8 |\n"
        "| Family discount | £1 per extra member |\n"
        "| Family pack discount | 5% |\n"
        "| Dual‑service loyalty discount | 10% |"
    )

with model_col2:
    st.subheader("Posting Fees")
    st.markdown(
        "| Reach | Fee |\n"
        "| --- | --- |\n"
        "| Local | £0 |\n"
        "| Regional | £5 |\n"
        "| National | £10 |\n"
        "| International | £15 |\n"
        "| Family discounts | Apply |"
    )

with model_col3:
    st.subheader("Points System")
    st.markdown(
        "| Item | Value |\n"
        "| --- | --- |\n"
        "| Points per thumbs‑up | 20 |\n"
        "| Thumbs‑up per month | 50 |\n"
        "| Points per member | 1,000 |\n"
        "| Points per team | 4,000 |\n"
        "| Points per referral | 20 |\n"
        "| Max members per family | 2 |"
    )

st.success("Everything is now internally consistent.")

# ── Navigation links ──────────────────────────────────────────────────────────
st.divider()
st.subheader("Platform Sections")
nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    st.page_link("pages/1_Release_Hub.py", label="📅 Release Hub")
    st.page_link("pages/2_Genres.py", label="🎭 Genre Rotation")
with nav_col2:
    st.page_link("pages/3_Artists.py", label="🎨 Artist Pages")
    st.page_link("pages/4_Events.py", label="🎉 Events & Parties")
with nav_col3:
    st.page_link("pages/17_Analytics.py", label="📊 Analytics")
    st.page_link("pages/18_Moment_Map.py", label="🗺️ Moment Map")