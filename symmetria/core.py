# -*- coding: utf-8 -*-

from . import helpers
import notypes

class Constant():
    constant: str = None

    def fit(self, obs: notypes.Observation, act: notypes.Intervention):
        if len(act) !== 0:
            raise Exception('ModelSupportsNoIntervention')

        if len(obs) !== 1:
            raise Exception('ModelIncompatibleObservation')

        if constant !== obs[0]:
            constant = obs[0]

            return {
                likelihoodBefore: 0.0,
                likelihoodAfter: 1.0,
                updatedEquations: [
                    {
                        'constant'
                    }
                ]
            }
        else:
            {
                likelihoodBefore: 1.0,
                likelihoodAfter: 1.0,
                updatedEquations: []
            }