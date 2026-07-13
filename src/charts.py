"""
=========================================================
Charts
Mini Network IDS
=========================================================

Creates Plotly charts for the Streamlit Dashboard.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# =========================================================
# Protocol Distribution
# =========================================================

def protocol_chart(stats):

    labels = [
        "TCP",
        "UDP",
        "ICMP",
        "ARP",
        "IPv6"
    ]

    values = [
        stats.get("tcp", 0),
        stats.get("udp", 0),
        stats.get("icmp", 0),
        stats.get("arp", 0),
        stats.get("ipv6", 0)
    ]

    # Prevent empty chart
    if sum(values) == 0:
        labels = ["No Traffic"]
        values = [1]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.45,
        title="Protocol Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title="Protocols"
    )

    return fig


# =========================================================
# Live Traffic Timeline
# =========================================================

def traffic_chart(history):

    if not history:

        fig = go.Figure()

        fig.update_layout(
            template="plotly_dark",
            title="Live Traffic",
            height=420
        )

        return fig

    timestamps = [row[0] for row in history]

    df = pd.DataFrame({
        "Packet": range(1, len(timestamps) + 1),
        "Timestamp": timestamps
    })

    fig = px.line(
        df,
        x="Packet",
        y="Packet",
        markers=True,
        title="Traffic Timeline"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        xaxis_title="Captured Packets",
        yaxis_title="Packet Count"
    )

    return fig


# =========================================================
# Top Source IPs
# =========================================================

def top_source_chart(rows):

    if not rows:

        fig = go.Figure()

        fig.update_layout(
            template="plotly_dark",
            title="Top Source IPs",
            height=420
        )

        return fig

    df = pd.DataFrame(
        rows,
        columns=["Source IP", "Packets"]
    )

    fig = px.bar(
        df,
        x="Source IP",
        y="Packets",
        title="Top Source IPs"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    return fig


# =========================================================
# Top Destination IPs
# =========================================================

def top_destination_chart(rows):

    if not rows:

        fig = go.Figure()

        fig.update_layout(
            template="plotly_dark",
            title="Top Destination IPs",
            height=420
        )

        return fig

    df = pd.DataFrame(
        rows,
        columns=["Destination IP", "Packets"]
    )

    fig = px.bar(
        df,
        x="Destination IP",
        y="Packets",
        title="Top Destination IPs"
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    return fig