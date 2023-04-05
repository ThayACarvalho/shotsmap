import streamlit as st
import mplsoccer 
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import statsbombpy as sb
from statsbombpy import sb
from mplsoccer import VerticalPitch

danny_ings = '/folder/Danny_Ings.csv'
gareth_bale = '/folder/Gareth_Bale.csv')
james_maddison = '/folder/James_Maddison.csv')
jesse_lingard = '/folder/Jesse_Lingard.csv')
son_heung = '/folder/Son_Heung-Min.csv')

emile_smith = '/folder/Emile_Smith-Rowe.csv')
james_maddison22 = '/folder/James_Maddison.csv')
James_ward = '/folder/James_Ward-Prowse.csv')
kevin_bruyne = '/folder/Kevin_de_Bruyne.csv')
son_heung22 = '/folder/Son_Heung-Min.csv')

st.title('Premier League Top Shooters Shotmap')

st.sidebar.title('Escolha o jogador')
Pagina_selecionada = st.sidebar.selectbox('Selecione um jogador', ['Danny Ings 2020-2021', 'Gareth Bale 2020-2021', 'James Maddison 2020-2021', 'Jesse Lingard 2020-2021', 'Son Heung-Min 2020-2021', 'Emile Smith 2021-2022', 'James Maddison 2021-2022', 'James Ward 2021-2022', 'Kevin de Bruyne 2021-2022', 'Son Heung-Min 2021-2022'])

if Pagina_selecionada == 'Danny Ings 2020-2021':
    player_goal = danny_ings[danny_ings['result'] == 'Goal'].copy()
    player_nogoal = danny_ings[danny_ings['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'Gareth Bale 2020-2021':
    player_goal = gareth_bale[gareth_bale['result'] == 'Goal'].copy()
    player_nogoal = gareth_bale[gareth_bale['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'James Maddison 2020-2021':
    player_goal = james_maddison[james_maddison['result'] == 'Goal'].copy()
    player_nogoal = james_maddison[james_maddison['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'Jesse Lingard 2020-2021':
    player_goal = jesse_lingard[jesse_lingard['result'] == 'Goal'].copy()
    player_nogoal = jesse_lingard[jesse_lingard['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'Son Heung-Min 2020-2021':
    player_goal = son_heung[son_heung['result'] == 'Goal'].copy()
    player_nogoal = son_heung[son_heung['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'Emile Smith 2021-2022':
    player_goal = emile_smith[emile_smith['result'] == 'Goal'].copy()
    player_nogoal = emile_smith[emile_smith['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'James Maddison 2021-2022':
    player_goal = james_maddison22[james_maddison22['result'] == 'Goal'].copy()
    player_nogoal = james_maddison22[james_maddison22['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'James Ward 2021-2022':
    player_goal = James_ward[James_ward['result'] == 'Goal'].copy()
    player_nogoal = James_ward[James_ward['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)



if Pagina_selecionada == 'Kevin de Bruyne 2021-2022':
    player_goal = kevin_bruyne[kevin_bruyne['result'] == 'Goal'].copy()
    player_nogoal = kevin_bruyne[kevin_bruyne['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))

    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)

if Pagina_selecionada == 'Son Heung-Min 2021-2022':
    player_goal = son_heung22[son_heung22['result'] == 'Goal'].copy()
    player_nogoal = son_heung22[son_heung22['result'] != 'Goal'].copy()
    
    pitch = VerticalPitch(half=True)
    fig, ax = pitch.draw(figsize=(5, 5))
    
    goal = pitch.scatter(player_goal["NewX"], player_goal["NewY"], color='blue', label='Goal', ax=ax)

    nogoal = pitch.scatter(player_nogoal["NewX"], player_nogoal["NewY"], color='red', label='No Goal', ax=ax)
    ax.legend()
    st.pyplot(fig,ax)
