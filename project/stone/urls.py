from django.contrib import admin
from django.urls import path,include
from stone import views

urlpatterns = [
    path('',views.index,name='index'),

    path('contact',views.contact,name='contact'), 

    path('about',views.about,name='about'),

    path('signup',views.signup,name='auth/signup'), 

    path('login',views.handlelogin,name='handlelogin'),

    path('logout',views.handlelogout,name='handlelogout'),

    path('kadapablack',views.kadapablack,name='kadapablack'), 

    path('KarnoolGray',views.KarnoolGray,name='KarnoolGray'), 

    path('LimeStones',views.LimeStones,name='LimeStones'), 

    path('TandurBlue',views.TandurBlue,name='TandurBlue'), 

    path('TandurYellow',views.TandurYellow,name='TandurYellow'), 

    path('MosaicTiles',views.MosaicTiles,name='MosaicTiles'), 

    path('StonePebbles',views.StonePebbles,name='StonePebbles'),

    path('StoneVenus',views.StoneVenus,name='StoneVenus'), 

    path('WindowSills',views.WindowSills,name='WindowSills'), 

    path('BlockSteps',views.BlockSteps,name='BlockSteps'), 

    path('Cobbles',views.Cobbles,name='Cobbles'), 

    path('FlagStone',views.FlagStone,name='FlagStone'), 

    path('KerbStones',views.KerbStones,name='KerbStones'), 

    path('Palisader',views.Palisader,name='Palisader'), 

    path('PoolCoping',views.PoolCoping,name='PoolCoping'), 

    path('RoofingTiles',views.RoofingTiles,name='RoofingTiles'), 

    path('StonePaving',views.StonePaving,name='StonePaving'), 

    path('StoneQuoins',views.StoneQuoins,name='StoneQuoins'),

    path('PierCaps',views.PierCaps,name='PierCaps'), 

    #path('search',views.search,name='search'),
    
    path('services',views.services,name='services'), 

    path('gallery',views.gallery,name='gallery'), 

    path('search',views.search,name='search'),
    

]
