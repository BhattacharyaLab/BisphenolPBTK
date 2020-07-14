import pandas as pd
import tellurium as te


class Experiment(object):
    model = None
    variables = ['time']
    
    def __init__(self, start=0, end=48, steps=2001):
        self.model = open(self.model, 'r').read()
        self.runner = te.loada(self.model)
        self.start = start
        self.end = end
        self.steps = steps
        
    def param_init(self):
        raise NotImplementedError(
            'Method param_init not implemented. ' + 
            'Should be used to set the initial value of experiment specific parameters.'
        )
        
    def set_params(self, params):
        for param in params:
            if not hasattr(self.runner, param):
                raise RuntimeError('Parameter: %s does not exist' % param)
            setattr(self.runner, param, float(params[param]))
    
    def reset(self, params=dict()):
        params = params.copy()
        
        self.runner.resetToOrigin()
        
        params.update(
            self.param_init()
        )
        self.set_params(params)
        
        self.runner.reset()
        
    def run(self, as_dataframe=False, params={}):
        self.reset(params)
        self.runner.selections = self.variables
        sim = self.runner.simulate(self.start, self.end, self.steps)
        if as_dataframe:
            sim = pd.DataFrame(sim, columns=self.variables)
        return sim
    
    def plot(self, params={}):
        sim = self.run(params=params)
        self.runner.plot(sim)
    
     
class VeigaLopezExperiment(Experiment):
    model = '../BPS_model.txt' 
    variables = ['time', 'CAtotal_ngml', 'CEFtotal_ngml', 'CA_ngml', 'CAconj_ngml', 'CEF_ngml', 'CEFconj_ngml']
    
    def param_init(self):
        return {
            'BW': 76.25,
            'PDOSE': 0.5e-3,
        }

    
class MultiSCExperiment(Experiment):
    model = '../BPS_model.txt' 
    variables = ['time', 
                 'CAtotal_ngml', 'CEFtotal_ngml',
                 'CA_ngml', 'CAconj_ngml', 
                 'CEF_ngml', 'CEFconj_ngml',
                 'fBPS_nmol_total',
                 'fBPSconj_nmol_total',
                 'fBPS_ngml_total',
                 'fBPSconj_ngml_total',
    ]
    
    def param_init(self):
        return {
            'BW': 76.25,
            #'PSCDOSE_mBPA': 0.5e-3,
        }
        

    
class GrandinExperiment1_Mother_BPSG(Experiment):
    model = '../BPS_model.txt' 
    variables = ['time', 
                 'CA_uM', 'CA_conj_uM', 'CEF_uM', 'CEF_conj_uM', 
                 'CA_d8_uM', 'CA_conj_d8_uM', 'CEF_d8_uM', 'CEF_conj_d8_uM',
                 'CA_ngml', 'CAconj_ngml', 'CEF_ngml', 'CEFconj_ngml',
                 'CA_d8_ngml', 'CAconj_d8_ngml', 'CEF_d8_ngml', 'CEFconj_d8_ngml',
    ]
    
    def param_init(self):
        return {
            #'BW': 79,                    # +/- 15kg
            'PIV_conj_BOLUS': 6.3e-6,    #umol/kg
            'PIV_d8_BOLUS': 19.4e-6,     #umol
        }
    

class GrandinExperiment2_Mother_BPS(Experiment):
    model = '../BPS_model.txt' 
    variables = ['time', 
                 'CA_uM', 'CA_conj_uM', 'CEF_uM', 'CEF_conj_uM', 
                 'CA_d8_uM', 'CA_conj_d8_uM', 'CEF_d8_uM', 'CEF_conj_d8_uM',
                 'CA_ngml', 'CAconj_ngml', 'CEF_ngml', 'CEFconj_ngml',
                 'CA_d8_ngml', 'CAconj_d8_ngml', 'CEF_d8_ngml', 'CEFconj_d8_ngml',
    ]
    
    def param_init(self):
        return {
            #'BW': 79,                      # +/- 15kg
            'PIV_BOLUS': 20e-6,            #umol/kg
            'PIV_conj_d8_BOLUS': 40.3e-6,     #umol
        }

#
#class CorbelExperiment_Mother_BPAG(Experiment):
#    model = '../BPA_model.txt' 
#    variables = ['time', 'CA_nM', 'CA_conj_nM', 'CA_fetus_nM', 'CA_conj_fetus_nM']
#    
#    def param_init(self):
#        return {
#            'BW': 45.67,
#            'PIV_conj_DOSE': 3.54e-3,
#        }
#            
#        
#class CorbelExperiment_Fetus_BPA(Experiment):
#    model = '../BPA_model.txt' 
#    variables = ['time', 'CA_nM', 'CA_conj_nM', 'CA_fetus_nM', 'CA_conj_fetus_nM']
#    
#    def param_init(self):
#        return {
#            'BW': 45.67,
#            'PIV_fetal_DOSE': 5e-3 / 1.6,
#        }
#        
#        
#class CorbelExperiment_Fetus_BPAG(Experiment):
#    model = '../BPA_model.txt' 
#    variables = ['time', 'CA_nM', 'CA_conj_nM', 'CA_fetus_nM', 'CA_conj_fetus_nM']
#    
#    def param_init(self):
#        return {
#            'BW': 45.67,
#            'PIV_conj_fetal_DOSE': 3.54e-3 / 1.6,
#        }
