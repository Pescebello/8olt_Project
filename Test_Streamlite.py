#    []   {}   |

import plotly.express as px
import streamlit as st
from Database import df

st.set_page_config(page_title='ßolt Customer Support Analytics', page_icon='🛴', layout='wide')

col_logo, col_title = st.columns([1, 4], vertical_alignment='center')

col_logo.image('vecteezy_customer-satisfaction-icon-style_13695803.jpg')

col_title.title('ßolt Operations Dashboard')

st.caption("<p style='text-align: center;'>Real-time performance metrics tracking resolution efficiency, CSAT, and market distribution.</p>",
    unsafe_allow_html=True,)

st.divider()
Clean_df = df.rename(
    columns={
        'channel': 'Communication Channel',
        'language': 'Market Language',
        'priority': 'Ticket Priority',
        'customer_tier': 'Customer Tier',
        'category': 'Issue Category',
        'resolution_time_min': 'Resolution Time (min)',
        'csat': 'CSAT Score',
    }
)

languages = st.sidebar.multiselect(
    label='Filter by Market Language',
    options=Clean_df['Market Language'].unique(),
    default=['Italian', 'English', 'Estonian'],
)

channel = st.sidebar.multiselect(
    label='Filter by Channel',
    options=Clean_df['Communication Channel'].unique(),
    default=['Email', 'Live Chat', 'Web Form', 'In-App Ticket'],
)

customer_tier = st.sidebar.multiselect(
    label='Filter by Customer Tier',
    options=Clean_df['Customer Tier'].unique(),
    default=['Free', 'Standard', 'Premium'],
)

priority = st.sidebar.multiselect(
    label='Filter by Priority',
    options=Clean_df['Ticket Priority'].unique(),
    default=['Low', 'Medium', 'High', 'Urgent'],
)


filtered_df = Clean_df[
    Clean_df['Communication Channel'].isin(channel)
    & Clean_df['Customer Tier'].isin(customer_tier)
    & Clean_df['Ticket Priority'].isin(priority)
    & Clean_df['Market Language'].isin(languages)
]
if filtered_df.empty:
    st.warning('⚠️No tickets match the selected filters.')

else:
    m_col1, m_col2, m_col3 = st.columns(3)

    avg_csat = filtered_df['CSAT Score'].mean()
    avg_res_time = filtered_df['Resolution Time (min)'].mean()
    total_tickets = len(filtered_df)

    m_col1.write(f'**Total Tickets:** {total_tickets:}')
    m_col2.write(f'**Average CSAT Score** {avg_csat:.1f} / 5.0')
    m_col3.write(f'**Avg Resolution Time** {avg_res_time:.1f} mins')

    st.divider()

    st.write('📊 **Dynamic Analytical Charts**')

    top_col1, top_col2 = st.columns([1, 1], vertical_alignment='center')

    with top_col1:
        st.write('**Performance Controls**')

        x_axis_choice = st.selectbox(
            'Group by:',
            options=[
                    'Communication Channel',
                    'Market Language',
                    'Ticket Priority',
                    'Customer Tier',
                    'Issue Category',
            ],
            index=0,
        )
        y_axis_choice = st.selectbox(
            'Measure by:',
            options=['Resolution Time (min)', 'CSAT Score'],
            index=0,)

    with top_col2:
        st.write('**Volume Breakdown**')

        fig_sunburst = px.sunburst(
            filtered_df,
            path=[x_axis_choice] if x_axis_choice == 'Customer Tier' else [x_axis_choice, 'Customer Tier'],
            values=y_axis_choice,
            color_discrete_sequence=px.colors.sequential.Tealgrn,
            title=f'Ticket Distribution Volume Share by {x_axis_choice.title()}',
            height=550,
        )
        fig_sunburst.update_traces(
            textinfo='label+value',
            textfont_size=12
        )

        st.plotly_chart(fig_sunburst, use_container_width=True)

    st.write('**Performance Overview**')

    fig_dynamic = px.histogram(
        filtered_df,
        x=x_axis_choice,
        y=y_axis_choice,
        color='Issue Category',
        barmode='group',
        histfunc='avg',
        text_auto='.1f',
        color_discrete_sequence=px.colors.qualitative.Set3,
        title=f"Average {y_axis_choice.replace('_', ' ').title()} by {x_axis_choice.title()}"
    )

    st.plotly_chart(fig_dynamic, use_container_width=True)

    st.divider()

    tab1, tab2 = st.tabs(['📉 Operational Benchmarks', '📋 Raw Data Inspector'])
    with tab1:
        st.write('**Volume by Channel**')
        fig = px.histogram(
            filtered_df,
            x='CSAT Score',
            color='Communication Channel',
            barmode='group',
            log_y=True,
            color_discrete_sequence=['#10B981', '#39FF14', '#CCFF00', '#FFF01F', '#FFE600'],
            text_auto=True,
            height=320
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.write("**Filtered Ticket Data View**")
        cols = ['tickets_ID',
                'created_at',
                'Issue Category',
                'Market Language',
                'Ticket Priority',
                'Communication Channel',
                'Customer Tier',
                'Resolution Time (min)',
                'CSAT Score',]
        st.dataframe(filtered_df[cols])
