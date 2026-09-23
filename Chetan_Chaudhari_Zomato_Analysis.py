"""
Chetan_Chaudhari_Zomato_Analysis.py
-------------------------------------
Main Python script for Zomato Restaurant & Customer Insights Analysis.
Runs the full analytics pipeline: load → clean → engineer → analyse → insight.
Saves cleaned data and prints results to console.

Author  : Chetan Chaudhari
Project : Zomato Restaurant & Customer Insights Analysis
          Data Analytics Internship Project
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from collections import Counter

# ── paths ────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR    = os.path.join(SCRIPT_DIR, "src")
DATA_DIR   = os.path.join(SCRIPT_DIR, "data")
VIZ_DIR    = os.path.join(SCRIPT_DIR, "visualizations")
os.makedirs(VIZ_DIR, exist_ok=True)

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from data_cleaning  import load_raw_data, clean_data, engineer_features, save_cleaned_data
from analysis       import (
    get_kpis, restaurants_by_city, restaurants_by_price_category,
    top_individual_cuisines, cuisine_avg_rating,
    rating_distribution, avg_rating_by_city, avg_rating_by_price,
    top_restaurants_by_votes, top_rated_restaurants,
    avg_cost_by_city, avg_cost_by_price_category,
    delivery_by_city, booking_by_price, delivery_by_price,
    rating_by_delivery, rating_by_booking,
    correlation_matrix, descriptive_stats,
    high_rated_high_votes,
)
from insights import generate_insights, executive_summary

# ── styling ──────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="Reds_r")
plt.rcParams.update({"figure.dpi": 100, "font.size": 11})

REDS = ["#d32f2f", "#e53935", "#ef9a9a", "#ffcdd2", "#b71c1c"]

# ══════════════════════════════════════════════════════════════════════════
# SECTION 1 — LOAD DATA
# ══════════════════════════════════════════════════════════════════════════

def load_and_profile():
    raw_path = os.path.join(DATA_DIR, "raw", "zomato.csv")
    print("=" * 70)
    print("  ZOMATO RESTAURANT & CUSTOMER INSIGHTS ANALYSIS")
    print("  Author: Chetan Chaudhari  |  Data Analytics Internship Project")
    print("=" * 70)
    print("\n[1] LOADING DATASET")
    df_raw = load_raw_data(raw_path)
    print(f"    Shape  : {df_raw.shape}")
    print(f"    Columns: {list(df_raw.columns)}")
    print("\n[2] DATASET PROFILE")
    print("    Missing values:")
    print(df_raw.isnull().sum())
    print(f"    Duplicate rows: {df_raw.duplicated().sum()}")
    print("\n    Descriptive statistics:")
    print(df_raw.describe().round(2))
    return df_raw


# ══════════════════════════════════════════════════════════════════════════
# SECTION 2 — CLEAN & ENGINEER
# ══════════════════════════════════════════════════════════════════════════

def clean_and_engineer(df_raw: pd.DataFrame) -> pd.DataFrame:
    print("\n[3] DATA CLEANING")
    df_clean = clean_data(df_raw)
    print("\n[4] FEATURE ENGINEERING")
    df = engineer_features(df_clean)
    cleaned_path = os.path.join(DATA_DIR, "cleaned", "zomato_cleaned.csv")
    save_cleaned_data(df, cleaned_path)
    return df


# ══════════════════════════════════════════════════════════════════════════
# SECTION 3 — KPIs
# ══════════════════════════════════════════════════════════════════════════

def print_kpis(df: pd.DataFrame):
    print("\n[5] KEY PERFORMANCE INDICATORS")
    kpis = get_kpis(df)
    for k, v in kpis.items():
        print(f"    {k:35s}: {v}")


# ══════════════════════════════════════════════════════════════════════════
# SECTION 4 — VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════

def save_fig(name: str):
    path = os.path.join(VIZ_DIR, name)
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    print(f"    Saved: {path}")


def plot_restaurants_by_city(df: pd.DataFrame):
    data = restaurants_by_city(df, top_n=15)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["City"], data["count"], color=REDS[0])  # 'count' from value_counts()
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_xlabel("Number of Restaurants")
    ax.set_title("Top 15 Cities by Restaurant Count")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("01_restaurants_by_city.png")


def plot_top_cuisines(df: pd.DataFrame):
    data = top_individual_cuisines(df, top_n=15)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["Cuisine"], data["Count"], color=REDS[0])
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_xlabel("Number of Restaurants")
    ax.set_title("Top 15 Most Common Cuisines")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("02_top_cuisines.png")


def plot_rating_distribution(df: pd.DataFrame):
    rated = df[df["Aggregate rating"] > 0]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(rated["Aggregate rating"], bins=20, color=REDS[0], edgecolor="white")
    ax.set_xlabel("Aggregate Rating")
    ax.set_ylabel("Number of Restaurants")
    ax.set_title("Rating Distribution (Rated Restaurants)")
    plt.tight_layout()
    save_fig("03_rating_distribution.png")


def plot_price_category_distribution(df: pd.DataFrame):
    data = restaurants_by_price_category(df)
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(data["Price Category"], data["Count"], color=REDS[:4])
    ax.bar_label(bars, padding=3)
    ax.set_xlabel("Price Category")
    ax.set_ylabel("Count")
    ax.set_title("Restaurant Count by Price Category")
    plt.tight_layout()
    save_fig("04_price_category_distribution.png")


def plot_online_delivery(df: pd.DataFrame):
    od = df["Has Online delivery"].map({1:"Yes",0:"No"}).value_counts()
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(od, labels=od.index, autopct="%1.1f%%",
           colors=[REDS[0], REDS[2]], startangle=90)
    ax.set_title("Online Delivery Availability")
    plt.tight_layout()
    save_fig("05_online_delivery.png")


def plot_table_booking(df: pd.DataFrame):
    tb = df["Has Table booking"].map({1:"Yes",0:"No"}).value_counts()
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(tb, labels=tb.index, autopct="%1.1f%%",
           colors=[REDS[1], REDS[3]], startangle=90)
    ax.set_title("Table Booking Availability")
    plt.tight_layout()
    save_fig("06_table_booking.png")


def plot_rating_by_price(df: pd.DataFrame):
    data = avg_rating_by_price(df)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(data["Price Category"], data["Avg Rating"], color=REDS[:4])
    ax.bar_label(bars, padding=3)
    ax.set_ylim(0, 5.5)
    ax.set_xlabel("Price Category")
    ax.set_ylabel("Average Rating")
    ax.set_title("Average Rating by Price Category")
    plt.tight_layout()
    save_fig("07_rating_by_price.png")


def plot_avg_cost_by_city(df: pd.DataFrame):
    data = avg_cost_by_city(df, top_n=15, min_count=10)
    if data.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["City"], data["Avg Cost for Two"], color=REDS[0])
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_xlabel("Average Cost for Two (₹)")
    ax.set_title("Average Cost for Two by City (Top 15)")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("08_avg_cost_by_city.png")


def plot_votes_vs_rating(df: pd.DataFrame):
    rated = df[df["Aggregate rating"] > 0]
    fig, ax = plt.subplots(figsize=(9, 6))
    scatter = ax.scatter(
        rated["Votes"], rated["Aggregate rating"],
        c=rated["Price range"], cmap="Reds",
        alpha=0.5, s=20,
    )
    plt.colorbar(scatter, ax=ax, label="Price Range")
    ax.set_xlabel("Votes")
    ax.set_ylabel("Aggregate Rating")
    ax.set_title("Votes vs Rating (coloured by Price Range)")
    plt.tight_layout()
    save_fig("09_votes_vs_rating.png")


def plot_delivery_by_city(df: pd.DataFrame):
    data = delivery_by_city(df, top_n=15, min_count=20)
    if data.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["City"], data["Online Delivery %"], color=REDS[0])
    ax.bar_label(bars, padding=3, fontsize=9, fmt="%.1f%%")
    ax.set_xlabel("Online Delivery %")
    ax.set_title("Online Delivery % by City (Top 15)")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("10_delivery_by_city.png")


def plot_booking_by_price(df: pd.DataFrame):
    data = booking_by_price(df)
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(data["Price Category"], data["Table Booking %"], color=REDS[:4])
    ax.bar_label(bars, padding=3, fmt="%.1f%%")
    ax.set_xlabel("Price Category")
    ax.set_ylabel("Table Booking %")
    ax.set_title("Table Booking Availability by Price Category")
    plt.tight_layout()
    save_fig("11_booking_by_price.png")


def plot_top_voted(df: pd.DataFrame):
    data = top_restaurants_by_votes(df, top_n=15)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["Restaurant Name"], data["Votes"], color=REDS[0])
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_xlabel("Votes")
    ax.set_title("Top 15 Restaurants by Votes")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("12_top_voted_restaurants.png")


def plot_cuisine_avg_rating(df: pd.DataFrame):
    data = cuisine_avg_rating(df, top_n=15, min_count=20)
    if data.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["Cuisine"], data["Avg Rating"], color=REDS[0])
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_xlim(0, 5.5)
    ax.set_xlabel("Average Rating")
    ax.set_title("Average Rating by Cuisine (Top 15, min 20 restaurants)")
    ax.invert_yaxis()
    plt.tight_layout()
    save_fig("13_cuisine_avg_rating.png")


def run_all_visualizations(df: pd.DataFrame):
    print("\n[6] GENERATING VISUALIZATIONS")
    plot_restaurants_by_city(df)
    plot_top_cuisines(df)
    plot_rating_distribution(df)
    plot_price_category_distribution(df)
    plot_online_delivery(df)
    plot_table_booking(df)
    plot_rating_by_price(df)
    plot_avg_cost_by_city(df)
    plot_votes_vs_rating(df)
    plot_delivery_by_city(df)
    plot_booking_by_price(df)
    plot_top_voted(df)
    plot_cuisine_avg_rating(df)


# ══════════════════════════════════════════════════════════════════════════
# SECTION 5 — INSIGHTS
# ══════════════════════════════════════════════════════════════════════════

def _safe_print(text: str):
    """Print with non-ASCII chars replaced to avoid Windows console encoding errors."""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", errors="replace").decode("ascii"))


def print_insights(df: pd.DataFrame):
    _safe_print("\n[7] AUTOMATED INSIGHTS")
    _safe_print("\n    Executive Summary:")
    _safe_print("    " + executive_summary(df))
    _safe_print("")
    for i, ins in enumerate(generate_insights(df), 1):
        _safe_print(f"  [{i}] {ins['title']}")
        _safe_print(f"       Metric         : {ins['metric'][:100]}")
        _safe_print(f"       Finding        : {ins['finding'][:120]}")
        _safe_print(f"       Recommendation : {ins['recommendation'][:120]}")
        _safe_print("")


# ══════════════════════════════════════════════════════════════════════════
# SECTION 6 — STATISTICAL ANALYSIS
# ══════════════════════════════════════════════════════════════════════════

def print_statistics(df: pd.DataFrame):
    print("\n[8] STATISTICAL ANALYSIS")
    print("\n    Descriptive Statistics:")
    print(descriptive_stats(df))
    print("\n    Correlation Matrix:")
    print(correlation_matrix(df))

    corr_rv = df["Aggregate rating"].corr(df["Votes"])
    corr_cr = df["Average Cost for two"].corr(df["Aggregate rating"])
    print(f"\n    Pearson r (Rating vs Votes)     : {corr_rv:.4f}")
    print(f"    Pearson r (Cost vs Rating)      : {corr_cr:.4f}")


# ══════════════════════════════════════════════════════════════════════════
# MAIN PIPELINE
# ══════════════════════════════════════════════════════════════════════════

def main():
    df_raw = load_and_profile()
    df     = clean_and_engineer(df_raw)
    print_kpis(df)
    run_all_visualizations(df)
    print_statistics(df)
    print_insights(df)
    print("\n" + "=" * 70)
    print("  PIPELINE COMPLETE")
    print(f"  Cleaned data : {os.path.join(DATA_DIR, 'cleaned', 'zomato_cleaned.csv')}")
    print(f"  Charts       : {VIZ_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
