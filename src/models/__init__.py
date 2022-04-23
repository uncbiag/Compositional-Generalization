#!/usr/bin/env python
"""
Created by zhenlinx on 02/24/2022
"""
from .vae import VAE
from .disc_vae import DiscreteVAE
from .rec_disc_vae import RecurrentDiscreteVAE
from .beta_tcvae import BetaTCVAE
from .ae import AutoEncoder

vae_models = {
    'VAE': VAE,
    'DiscreteVAE': DiscreteVAE,
    'RecurrentDiscreteVAE': RecurrentDiscreteVAE,
    'BetaTCVAE': BetaTCVAE,
    'AE': AutoEncoder,
    }