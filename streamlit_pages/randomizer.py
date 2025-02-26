import streamlit as st

st.title('Randomizador de Plan to Watch')
st.subheader('A maneira mais fácil de escolher qual o próximo anime para ver!')

df = st.session_state['df']
df_plan_to_watch = df[df['my_status'] == 'plan_to_watch'].reset_index(drop=True)

if st.button('Randomizar'):
    
    sample = df_plan_to_watch.sample(n=1)
    st.header(sample['series_title'].values[0])
    st.subheader(f"Quantidade de episódios: {sample['series_episodes'].values[0]}")
    st.subheader(f"Nota média: {sample['series_mean'].values[0] if sample['series_mean'].values[0] > 0 else 'Não lançado'}")
    st.subheader(f"Estudio Produtor: {sample['series_studio'].values[0]}")
    st.subheader(f"Duração média por epísódio: {round(sample['average_episode_duration'].values[0]/60)} Minutos")
    generos = sample['genres'].values[0]
    generos= ', '.join(generos)
    st.subheader(f'Generos: { generos}')
