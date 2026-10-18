import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_master


st.set_page_config(
    page_title="ROOTED",
    page_icon="🌾",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --farm-forest: #31583c;
        --farm-wheat: #c69a43;
        --farm-line: #d9dfca;
    }

    .stApp,
    [data-testid="stAppViewContainer"] {
        background: #fbfaf5 !important;
    }

    [data-testid="stMain"] {
        background: #fbfaf5 !important;
    }

    [data-testid="stAppViewContainer"] {
        color: #39463d !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stWidgetLabel"] p,
    [data-testid="stCaptionContainer"] p,
    .stApp label {
        color: #39463d !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #5c5548 !important;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 0;
        padding-bottom: 4rem;
    }

    h1, h2, h3, h4 {
        color: var(--farm-forest) !important;
    }

    h2 {
        padding-top: 0.35rem;
    }

    [data-testid="stHeader"] {
        height: 0;
        background: transparent;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #f1f5e9, #fffdf6);
        border: 1px solid var(--farm-line);
        border-left: 5px solid var(--farm-wheat);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: 0 5px 18px rgba(49, 72, 46, 0.06);
    }

    [data-testid="stMetricValue"] {
        color: var(--farm-forest);
    }

    [data-testid="stMetricLabel"] {
        color: #665d4b;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 253, 247, 0.9);
        border-color: var(--farm-line) !important;
        border-radius: 18px !important;
        box-shadow: 0 5px 18px rgba(49, 72, 46, 0.06);
        padding: 0.25rem;
    }

    [data-testid="stAlert"],
    [data-testid="stExpander"] {
        border-radius: 16px;
    }

    [data-testid="stExpander"] {
        background: rgba(255, 253, 247, 0.7);
        border: 1px solid var(--farm-line);
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
    div[data-baseweb="select"] > div {
        background: #fffdf7 !important;
        border-color: #cbd5bd !important;
        border-radius: 12px;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] *,
    [data-testid="stMultiSelect"] [data-baseweb="select"] *,
    div[data-baseweb="select"] [role="combobox"] {
        background: #fffdf7 !important;
        color: #39463d !important;
    }

    [data-baseweb="tag"] {
        background: #e8eedf !important;
        border: 1px solid #cbd5bd !important;
        border-radius: 8px !important;
        color: #31583c !important;
    }

    [data-baseweb="tag"] *,
    [data-baseweb="tag"] svg {
        background: transparent !important;
        color: #31583c !important;
        fill: #31583c !important;
    }

    [data-baseweb="popover"] > div,
    [data-baseweb="menu"],
    [role="listbox"] {
        background: #fffdf7 !important;
        color: #39463d !important;
    }

    [role="option"] {
        background: #fffdf7 !important;
        color: #39463d !important;
    }

    [role="option"]:hover,
    [aria-selected="true"][role="option"] {
        background: #e8eedf !important;
        color: #31583c !important;
    }

    div[data-testid="stRadio"] label {
        color: var(--farm-forest);
    }

    .stButton > button {
        background: var(--farm-forest);
        color: #fffdf5 !important;
        border: 1px solid var(--farm-forest);
        border-radius: 999px;
        font-weight: 650;
        transition: background 140ms ease, transform 140ms ease;
    }

    .stButton > button:hover {
        background: #456c49;
        border-color: #456c49;
        color: white !important;
        transform: translateY(-1px);
    }

    .site-nav {
        width: 100vw;
        margin-left: calc(50% - 50vw);
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.85rem max(1.5rem, calc((100vw - 1200px) / 2));
        background: #fff;
        border-bottom: 1px solid #e6e7e0;
    }

    .site-brand {
        color: #263f31 !important;
        font-size: 1.55rem;
        font-weight: 750;
        text-decoration: none !important;
        letter-spacing: -0.04em;
        white-space: nowrap;
    }

    .site-brand-mark {
        color: #69a92d;
    }

    .site-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 1.25rem;
    }

    .site-links a {
        color: #3f4540 !important;
        font-weight: 600;
        text-decoration: none !important;
    }

    .site-links a:hover {
        color: #57952e !important;
    }

    .section-anchor {
        scroll-margin-top: 5rem;
    }

    hr {
        border-color: var(--farm-line) !important;
    }

    .welcome {
        position: relative;
        overflow: hidden;
        display: grid;
        place-items: center;
        width: 100vw;
        min-height: 500px;
        margin-left: calc(50% - 50vw);
        margin-bottom: 0;
        border: 0;
        border-radius: 0;
        background: #243d2d;
        text-align: center;
    }

    .hero-video {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .welcome:before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(
            90deg,
            rgba(12, 31, 19, 0.76),
            rgba(18, 39, 23, 0.62) 52%,
            rgba(12, 31, 19, 0.76)
        );
        z-index: 1;
    }

    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 820px;
        padding: 4rem 1.5rem;
        color: #fff;
    }

    .welcome .hero-kicker {
        margin: 0 0 1rem;
        color: #fff !important;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.95);
    }

    .welcome h1 {
        margin: 0 auto;
        color: white !important;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.5rem, 5.3vw, 4.4rem);
        line-height: 1.08;
        max-width: 760px;
        text-shadow: 0 3px 14px rgba(0, 0, 0, 0.65);
    }

    .welcome .hero-content p {
        color: #fff !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.95);
    }

    .welcome .hero-content > p:not(.hero-kicker):not(.hero-note) {
        margin: 1.25rem auto 0;
        max-width: 680px;
        font-size: clamp(1rem, 1.8vw, 1.25rem);
        line-height: 1.55;
    }

    a.hero-cta {
        display: inline-block;
        margin-top: 1.6rem;
        padding: 0.8rem 1.65rem;
        border-radius: 12px;
        background: #fff;
        color: #3e4a3e !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        font-family: Georgia, "Times New Roman", serif;
        font-size: 1.15rem;
        font-weight: 700;
        text-decoration: none !important;
    }

    a.hero-cta:hover {
        background: #eff4e7;
        color: #31583c !important;
    }

    .welcome .hero-content .hero-note {
        margin-top: 1.4rem !important;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 0.95rem !important;
        font-weight: 700;
        letter-spacing: 0.04em;
    }

    @media (max-width: 640px) {
        .site-nav {
            justify-content: center;
            padding: 0.75rem 1rem;
        }

        .site-links {
            justify-content: center;
            gap: 0.8rem 1rem;
        }

        .welcome {
            min-height: 430px;
        }

    }

    @media (prefers-reduced-motion: reduce) {
        .hero-video {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def get_data():
    return load_master()


def production_chart(data, single_year):
    labels = {
        "year": "Year",
        "production_bu": "Production (bushels)",
        "County": "County",
    }

    if single_year:
        figure = px.bar(
            data,
            x="County",
            y="production_bu",
            color="County",
            labels=labels,
        )
        figure.update_layout(showlegend=False)

    else:
        figure = px.line(
            data.sort_values("year"),
            x="year",
            y="production_bu",
            color="County",
            markers=True,
            labels=labels,
        )
        figure.update_layout(
            hovermode="x unified",
            legend_title_text="",
        )

    figure.update_layout(
        height=330,
        margin=dict(t=20, b=20),
        template="plotly_white",
        paper_bgcolor="#fbfaf5",
        plot_bgcolor="#fbfaf5",
        font=dict(color="#39463d"),
        legend=dict(font=dict(color="#39463d")),
    )
    figure.update_xaxes(
        color="#39463d",
        tickfont_color="#39463d",
        gridcolor="#d9dfca",
        gridwidth=1,
        zeroline=False,
    )
    figure.update_yaxes(
        tickformat="~s",
        color="#39463d",
        tickfont_color="#39463d",
        gridcolor="#d9dfca",
        gridwidth=1,
        zeroline=False,
    )

    st.plotly_chart(figure, width="stretch")


st.markdown(
    """
    <nav class="site-nav" aria-label="Main navigation">
        <a class="site-brand" href="#page-top"><span class="site-brand-mark">🌱</span> ROOTED</a>
        <div class="site-links">
            <a href="#buying-area">Buying Areas</a>
            <a href="#backup-directory">Backup Areas</a>
            <a href="#plan-comparison">Compare Plans</a>
        </div>
    </nav>
    <div id="page-top"></div>
    <section class="welcome" aria-label="ROOTED introduction">
        <video class="hero-video" autoplay muted loop playsinline preload="metadata" aria-hidden="true">
            <source src="https://videos.pexels.com/video-files/32864188/14007563_4096_2160_24fps.mp4" type="video/mp4">
        </video>
        <div class="hero-content">
            <p class="hero-kicker">Data to Harvest · Delaware State University</p>
            <h1>🌾 ROOTED</h1>
            <p>Buying grain for your livestock? Explore your usual buying areas and find potential backups.</p>
            <a class="hero-cta" href="#buying-area">Explore buying areas</a>
            <p class="hero-note">Historical county-crop records, 2000–2025.</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

df = get_data().copy()
included_states = ["IA", "NE", "DE", "CA"]

required = {
    "fips",
    "county_name",
    "state_alpha",
    "year",
    "crop",
    "yield_status",
    "yield_per_acre",
    "acres_harvested",
}

missing = required - set(df.columns)

if missing:
    st.error("Missing data columns: " + ", ".join(sorted(missing)))
    st.stop()

for column in ["year", "yield_per_acre", "acres_harvested"]:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    ).astype(float)

crop_names = {
    "CORN": "Corn",
    "SOYBEANS": "Soybeans",
    "WHEAT": "Winter wheat",
    "SORGHUM": "Grain sorghum",
}

crop_options = sorted(
    df.loc[
        df["state_alpha"].isin(included_states),
        "crop",
    ].dropna().unique()
)

if not crop_options:
    st.warning("No crops are available for these states.")
    st.stop()


# STEP 1

st.markdown(
    '<div id="buying-area" class="section-anchor"></div>',
    unsafe_allow_html=True,
)
st.header("1. Where do you usually buy your grain?")

crop = st.selectbox(
    "Choose a crop",
    options=crop_options,
    format_func=lambda value: crop_names.get(value, value),
)
# Preserve reporting reasons before filtering production records.
record_status = df.loc[
    df["state_alpha"].isin(included_states)
    & df["crop"].eq(crop)
    & df["year"].between(2000, 2025)
    & df["fips"].notna(),
    ["fips", "year", "yield_status"],
].copy()

record_status["year"] = record_status["year"].astype(int)

# One lookup entry per county and year.
status_lookup = (
    record_status
    .drop_duplicates(["fips", "year"])
    .set_index(["fips", "year"])["yield_status"]
)
data = df.loc[
    df["state_alpha"].isin(included_states)
    & df["crop"].eq(crop)
    & df["year"].between(2000, 2025)
    & df["yield_status"].eq("reported")
    & df["fips"].notna()
    & np.isfinite(df["yield_per_acre"])
    & df["yield_per_acre"].gt(0)
    & np.isfinite(df["acres_harvested"])
    & df["acres_harvested"].gt(0)
].copy()

if data.duplicated(["fips", "year"]).any():
    st.error(
        "Duplicate county-year records were found. "
        "Please resolve them before continuing."
    )
    st.stop()

if data.empty:
    st.info(
        "No usable production records are available "
        "for this crop in the four included states."
    )
    st.stop()

coverage = data.groupby("fips")["year"].nunique()

# Keep this list for backup analysis only.
eligible = coverage.loc[coverage.eq(26)].index

data["year"] = data["year"].astype(int)
data["production_bu"] = (
    data["yield_per_acre"] * data["acres_harvested"]
)

county_options = (
    data[["fips", "county_name", "state_alpha"]]
    .drop_duplicates("fips")
    .sort_values(["state_alpha", "county_name"])
)

county_labels = {
    row.fips: f"{row.county_name}, {row.state_alpha}"
    for row in county_options.itertuples(index=False)
}

data["County"] = data["fips"].map(county_labels)

usual_counties = st.multiselect(
    "Choose your usual buying counties",
    options=county_options["fips"].tolist(),
    format_func=lambda value: county_labels[value],
    key=f"usual_{crop}",
)

view = st.radio(
    "Choose what to view",
    ["One year", "A time period"],
    horizontal=True,
)

if view == "One year":
    start_year = st.selectbox(
        "Year",
        options=list(range(2025, 1999, -1)),
    )
    end_year = start_year

else:
    start_year, end_year = st.slider(
        "Years",
        min_value=2000,
        max_value=2025,
        value=(2019, 2025),
    )

if not usual_counties:
    st.info("Choose a county to get started.")
    st.stop()

single_year = start_year == end_year
period = (
    str(start_year)
    if single_year
    else f"{start_year}–{end_year}"
)

period_data = data.loc[
    data["year"].between(start_year, end_year)
].copy()

usual_history = period_data.loc[
    period_data["fips"].isin(usual_counties)
].copy()

# Include every selected county-year so missing records stay visible.
expected_records = pd.MultiIndex.from_product(
    [
        usual_counties,
        range(start_year, end_year + 1),
    ],
    names=["fips", "year"],
)

usual_history = (
    usual_history
    .set_index(["fips", "year"])
    .reindex(expected_records)
    .reset_index()
)

usual_history["County"] = usual_history["fips"].map(
    county_labels
)
history_keys = pd.MultiIndex.from_frame(
    usual_history[["fips", "year"]]
)

history_status = status_lookup.reindex(
    history_keys
).to_numpy()

usual_history["Record note"] = np.select(
    [
        usual_history["production_bu"].notna().to_numpy(),
        history_status == "suppressed",
        history_status == "not_reported",
    ],
    [
        "Available",
        "Crop planted, but no grain harvested",
        "No yield estimate published",
    ],
    default="Usable yield or harvested-acre data is missing",
)
available_count = int(
    usual_history["production_bu"].notna().sum()
)

missing_count = int(
    usual_history["production_bu"].isna().sum()
)

if available_count == 0:
    st.info(
        "No usable production records are available for "
        "these counties during the selected years. "
        "Try another year or county."
    )

else:
    total = usual_history["production_bu"].sum(min_count=1)

    metric_label = (
        f"Production in available records • {period}"
        if missing_count
        else f"Produced in your selected counties • {period}"
    )

    st.metric(
        metric_label,
        f"{total:,.0f} bushels",
    )
    st.caption(
        "A bushel is a unit farmers use to measure "
        "the amount of grain harvested. Bushels are "
        "calculated as yield × harvested acres."
    )

    if missing_count:
        if single_year:
            st.warning(
                f"This total includes {available_count} of "
                f"your {len(usual_counties)} counties. "
                f"Data is missing for the others in {start_year}."
            )
        else:
            st.warning(
                f"This total includes {available_count} of "
                f"{len(usual_history)} yearly county records. "
                "Some records are missing."
            )

        st.caption(
            "Missing data does not mean no grain was grown."
        )

    elif not single_year:
        st.caption(
            "Total across all selected counties and years."
        )

    production_chart(usual_history, single_year)

with st.expander("See available and missing records"):
    record_table = usual_history[
        ["County", "year", "production_bu", "Record note"]
    ].rename(columns={
        "year": "Year",
        "production_bu": "Production (bushels)",
    })

    st.dataframe(
        record_table.style.format(
            {"Production (bushels)": "{:,.0f}"},
            na_rep="Not available",
        ),
        hide_index=True,
        width="stretch",
    )

st.caption(
    "County production (not the amount currently available to buy). "
    "Unavailable means a reported yield and/or valid harvested-acre "
    "record is missing."
)



# STEP 2

st.divider()
st.markdown(
    '<div id="backup-directory" class="section-anchor"></div>',
    unsafe_allow_html=True,
)
st.header("2. Where else could you look?")

backup_data = data.loc[
    data["fips"].isin(eligible)
].copy()

incomplete_usual = [
    fips
    for fips in usual_counties
    if fips not in eligible
]

if incomplete_usual:
    county_names = ", ".join(
        county_labels[fips]
        for fips in incomplete_usual
    )

    st.warning(
        f"Some past records are missing for: {county_names}."
    )

    st.write(
        "To find backups, remove these counties from your "
        "selection above. You can still view their available "
        "production records."
    )

    with st.expander("Why do we need these records?"):
        st.write(
            "Our backup test needs usable production records "
            "for every year from 2000–2025."
        )

    st.stop()

trend_rows = []

for fips, county in backup_data.groupby("fips"):
    county = county.sort_values("year").copy()

    training = county.loc[
        county["year"].between(2000, 2018)
    ]

    expected = training["production_bu"].mean()

    if (
        not np.isfinite(expected)
        or expected <= 0
    ):
        continue

    county["production_pct"] = 100 * county["production_bu"] / expected

    trend_rows.append(county)

if not trend_rows:
    st.info("There is not enough usable data to compare backups.")
    st.stop()

risk_data = pd.concat(trend_rows, ignore_index=True)

anomalies = (
    risk_data.pivot(
        index="year",
        columns="fips",
        values="production_pct",
    )
    .sort_index()
)

missing_usual = [
    fips
    for fips in usual_counties
    if fips not in anomalies.columns
]

if missing_usual:
    st.info(
        "We could not calculate average production for: "
        + ", ".join(county_labels[fips] for fips in missing_usual)
        + ". Try another county."
    )
    st.stop()

usual_index = anomalies[usual_counties].mean(axis=1)
training_index = usual_index.loc[2000:2018]
low_years = training_index.index[training_index.le(90)]

if len(low_years) == 0:
    st.info(
        "Your usual buying area had no low production years "
        "under our rule during 2000–2018. "
        "We cannot rank backups using shared low production years."
    )
    st.stop()

candidates = [
    fips
    for fips in anomalies.columns
    if fips not in usual_counties
]

if not candidates:
    st.info(
        "No other eligible counties remain. "
        "Try selecting fewer usual counties."
    )
    st.stop()

ranking_rows = []

for fips in candidates:
    values = anomalies.loc[low_years, fips]

    ranking_rows.append({
        "fips": fips,
        "overlap": int(values.le(90).sum()),
        "mean_production_pct": values.mean(),
    })

ranking = (
    pd.DataFrame(ranking_rows)
    .sort_values(
        ["overlap", "mean_production_pct", "fips"],
        ascending=[True, False, True],
    )
    .reset_index(drop=True)
)

top_backups = ranking.head(3)
top_ids = top_backups["fips"].tolist()

st.write(
    "These areas looked promising in the older records "
    "from 2000–2018. Compare one with your usual areas below."
)

if len(low_years) < 5:
    year_word = "year" if len(low_years) == 1 else "years"

    st.caption(
        f"We found only {len(low_years)} low production "
        f"{year_word} to compare in those older records."
    )

period_totals = period_data.groupby("fips")[
    "production_bu"
].sum()

columns = st.columns(len(top_backups))

for position, (column, row) in enumerate(
    zip(columns, top_backups.itertuples(index=False)),
    start=1,
):
    with column:
        with st.container(border=True):
            st.subheader(
                f"{position}. {county_labels[row.fips]}"
            )

            st.write(
                f"{period_totals.loc[row.fips]:,.0f} bushels "
                f"produced during {period}."
            )

            avoided = len(low_years) - row.overlap

            st.write("Why consider it?")

            st.write(
                f"It avoided low production in {avoided} "
                f"of the {len(low_years)} years when your "
                "usual buying area struggled."
            )

st.caption(
    "Potential buying areas—not confirmed sellers or available inventory."
)

with st.expander("How we chose these counties"):
    st.write(
        "We calculated each county's average annual production "
        "using records from 2000–2018."
    )
    st.write(
        "Low production means a county produced 90% or less of its 2000–2018 average."
    )
    st.write(
        "Candidates with fewer shared low production years rank first. "
    )
    st.write(
        "The production-year selector changes displayed totals, "
        "not the ranking period."
    )


# STEP 3

st.divider()
st.markdown(
    '<div id="plan-comparison" class="section-anchor"></div>',
    unsafe_allow_html=True,
)
st.header("3. Which plan had fewer low production years?")


backup_id = st.selectbox(
    "Choose another area to compare",
    options=top_ids,
    format_func=lambda value: county_labels[value],
    key=f"backup_{crop}",
)

st.write(
    "Stay with current county : use your usual area only.  \n"
    "Add a backup county : use mostly your usual area, "
    "plus some from the backup.  \n"
    "Switch counties entirely : use the selected backup area only."
)

st.caption("Based on production records from 2019–2025.")

# Calculate the three production-pattern plans.
test_years = list(range(2019, 2026))
number_of_years = len(test_years)

original = usual_index.reindex(test_years)
backup = anomalies[backup_id].reindex(test_years)
mixed = 0.75 * original + 0.25 * backup

test_values = np.column_stack([
    original.to_numpy(dtype=float),
    mixed.to_numpy(dtype=float),
    backup.to_numpy(dtype=float),
])

if not np.isfinite(test_values).all():
    st.warning(
        "Some records are missing. "
        "We cannot compare these plans right now."
    )
    st.stop()

original_low = int(original.le(90).sum())
mixed_low = int(mixed.le(90).sum())
backup_low = int(backup.le(90).sum())

chart_data = pd.DataFrame({
    "Plan": [
        "Stay with current county",
        "Add a backup county",
        "Switch counties entirely",
    ],
    "Low production years": [
        original_low,
        mixed_low,
        backup_low,
    ],
})

chart = px.bar(
    chart_data,
    x="Plan",
    y="Low production years",
    color="Plan",
    text="Low production years",
    category_orders={
        "Plan": [
            "Stay with current county",
            "Add a backup county",
            "Switch counties entirely",
        ],
    },
    color_discrete_map={
        "Stay with current county": "#8A6747",
        "Add a backup county": "#2F6844",
        "Switch counties entirely": "#C7A13B",
    },
)

chart.update_traces(
    textposition="outside",
    cliponaxis=False,
    hovertemplate=(
        "%{x}<br>"
        "Low production years: %{y} out of 7"
        "<extra></extra>"
    ),
)

chart.update_layout(
    height=320,
    showlegend=False,
    margin=dict(t=30, b=20, l=20, r=20),
    xaxis_title=None,
    yaxis_title="Low production years (out of 7)",
    template="plotly_white",
    paper_bgcolor="#fbfaf5",
    plot_bgcolor="#fbfaf5",
    font=dict(size=15, color="#39463d"),
)

chart.update_yaxes(
    range=[0, number_of_years + 1],
    tickmode="linear",
    dtick=1,
    fixedrange=True,
    color="#39463d",
    tickfont_color="#39463d",
    gridcolor="#d9dfca",
    gridwidth=1,
    zeroline=False,
)

chart.update_xaxes(
    fixedrange=True,
    color="#39463d",
    tickfont_color="#39463d",
    gridcolor="#d9dfca",
    gridwidth=1,
    zeroline=False,
)

st.plotly_chart(
    chart,
    width="stretch",
    config={"displayModeBar": False},
)

st.caption(
    "A shorter bar means fewer low production years."
)

# Report the lowest count, including ties.
fewest = int(chart_data["Low production years"].min())

best_plans = chart_data.loc[
    chart_data["Low production years"].eq(fewest),
    "Plan",
].tolist()

year_word = "year" if fewest == 1 else "years"

if len(best_plans) == 1:
    winner = best_plans[0]

    st.success(
        f"**{winner}** had the fewest low production "
        f"years in this test: {fewest} out of "
        f"{number_of_years}.\n\n"
        f"**GO WITH THIS OPTION — based on this past-data test.**"
    )

elif len(best_plans) == 2:
    st.info(
        f"**{best_plans[0]}** and **{best_plans[1]}** "
        f"tied for the fewest low production years: "
        f"{fewest} out of {number_of_years}.\n\n"
        "There is no single winner in this test. Choose one of these options."
    )

else:
    st.info(
        f"All three plans tied: {fewest} low production "
        f"{year_word} out of {number_of_years}.\n\n"
        "There is no single winner in this test."
    )

st.caption(
    "Our suggestion is based on past production. "
    "Before buying, check the seller's price, "
    "available grain, and delivery."
)

with st.expander("How did we test this?"):
    st.write(
        "We compared your usual area alone, a 75% usual-area "
        "/ 25% backup mix, and the backup area alone."
    )
    st.write(
        "We used 2000–2018 records to find possible backups. "
        "Then we compared the three plans using 2019–2025 records."
    )

    st.write(
        "The 'add a backup county' option uses 75% of your usual area's "
        "production pattern and 25% of the other area's. "
        "These are not actual purchases, just an example of what you can do."
    )

    st.write(
        "A low production year means the plan's production pattern "
        "was at 90% or less of its comparison baseline, calculated "
        "from 2000–2018 average production."
    )

    st.caption(
        "Only counties with complete 2000–2025 records are "
        "included. This is a look back to compare options "
        "based on prior production history."
    )

st.divider()



st.caption(
    "Before buying, confirm sellers, quantities, quality, prices, "
    "and delivery. ROOTED does not show live inventory "
    "or guarantee future supply."
)
