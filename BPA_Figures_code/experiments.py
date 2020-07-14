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
    model = '../BPA_model.txt' 
    variables = ['time', 'CA_plasma_ngml_mBPAtotal', 'CA_plasma_ngml_fBPAtotal', 'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_fBPA', 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPAconj']
    
    def param_init(self):
        return {
            'BW': 76.25,
            'PSCDOSE_mBPA': 0.5e-3,
        }

    
class MultiSCExperiment(Experiment):
    model = '../BPA_model.txt' 
    variables = ['time', 
                 'CA_plasma_ngml_mBPAtotal', 'CA_plasma_ngml_fBPAtotal', 
                 'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_fBPA', 
                 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPAconj',
                 'fBPA_nmol_total',
                 'fBPAconj_nmol_total',
                 'fBPA_ngml_total',
                 'fBPAconj_ngml_total',
    ]
    
    def param_init(self):
        return {
            'BW': 76.25,
            #'PSCDOSE_mBPA': 0.5e-3,
        }
    
        
class CorbelExperiment_Mother_BPA(Experiment):
    model = '../BPA_model.txt' 
    variables = [
            'time', 
            'CA_plasma_nM_mBPA', 'CA_plasma_nM_mBPAconj', 'CA_plasma_nM_fBPA', 'CA_plasma_nM_fBPAconj',
            'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPA', 'CA_plasma_ngml_fBPAconj'
    ]
    
    def param_init(self):
        return {
            'BW': 45.67,
            'PIVDOSE_mBPA': 2e-3,
        }
        

class CorbelExperiment_Mother_BPAG(Experiment):
    model = '../BPA_model.txt' 
    variables = [
            'time', 
            'CA_plasma_nM_mBPA', 'CA_plasma_nM_mBPAconj', 'CA_plasma_nM_fBPA', 'CA_plasma_nM_fBPAconj',
            'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPA', 'CA_plasma_ngml_fBPAconj'
    ]   

    
    def param_init(self):
        return {
            'BW': 45.67,
            'PIVDOSE_mBPAconj': 3.54e-3,
        }
            
        
class CorbelExperiment_Fetus_BPA(Experiment):
    model = '../BPA_model.txt' 
    variables = [
            'time', 
            'CA_plasma_nM_mBPA', 'CA_plasma_nM_mBPAconj', 'CA_plasma_nM_fBPA', 'CA_plasma_nM_fBPAconj',
            'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPA', 'CA_plasma_ngml_fBPAconj'
    ]   
    
    def param_init(self):
        return {
            'BW': 45.67,
            'PIVDOSE_fBPA': 5e-3,
        }
        
        
class CorbelExperiment_Fetus_BPAG(Experiment):
    model = '../BPA_model.txt' 
    variables = [
            'time', 
            'CA_plasma_nM_mBPA', 'CA_plasma_nM_mBPAconj', 'CA_plasma_nM_fBPA', 'CA_plasma_nM_fBPAconj',
            'CA_plasma_ngml_mBPA', 'CA_plasma_ngml_mBPAconj', 'CA_plasma_ngml_fBPA', 'CA_plasma_ngml_fBPAconj'
    ]   
   
    def param_init(self):
        return {
            'BW': 45.67,
            'PIVDOSE_fBPAconj': 3.54e-3,
        }
