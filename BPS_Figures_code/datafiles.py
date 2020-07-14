import pandas as pd


class Datafile(object):
    datafile = None
    title = None
    delimiter = ','
    header = None
    columns = None
    index_col = None
    
    mapping = {}
    
    def __init__(self, drop=None):
        self.df = pd.read_csv(
            self.datafile,
            delimiter=self.delimiter,
            header=self.header,
            names=self.columns,
            index_col=self.index_col,
        )
        
        if drop is not None:
            drop = drop + ['%s_Sd' % x for x in drop]
            self.df = self.df.drop(columns=drop)
        
        self.inv_mapping = {v: k for k, v in self.mapping.items()}
        
        # all the variables within the datafile
        #      excluding time and all the standard deviations
        self.variables = self.df.columns.copy()
        self.variables = self.variables[self.variables != 'time']
        self.variables = self.variables[~self.variables.str.endswith('_Sd')]

    def get_title(self, parameter):
        return self.title


class Datafile_VeigaLopez_Mother(Datafile):
    datafile = "../A006_BPS_Maternal.txt"
    delimiter = ','
    columns = ['time', 'C', 'C_Sd']
    title = 'Veiga-Lopez: Total BPS + BPSconj in mother [ng/ml]'
    
    mapping = {
        'CAtotal_ngml': 'C',
    }
    
    
class Datafile_VeigaLopez_Fetus(Datafile):
    datafile = "../A006_BPS_Fetal.txt"
    delimiter = ','
    header = None
    columns = ['time', 'C', 'C_Sd']
    title = 'Veiga-Lopez: Total BPA + BPAconj in fetus [ng/ml]'
    
    mapping = {
        'CEFtotal_ngml': 'C', 
    }
    
class Datafile_Grandin(Datafile):
    title = "Grandin (%s) - %s"

    
class Datafile_Grandin_Mother(Datafile_Grandin):
    """
    General structure of Grandin 2018 mother datafiles
   
    """
    mapping = {
        'CA_ngml': 'BPS',
        'CAconj_ngml': 'BPSG',
        'CA_d8_ngml': 'BPS-d8' , 
        'CAconj_d8_ngml': 'BPSG-d8',
    }
    header = 0
    index_col = 0

    def get_title(self, parameter):
        mapping = {
            'CA_ngml': 'mother BPS',
            'CAconj_ngml': 'mother BPSconj',
            'CA_d8_ngml': 'mother BPS-d8' , 
            'CAconj_d8_ngml': 'mother BPAconj-d8',
        }
     
        return self.title % (self.experiment, mapping[parameter]) 

    
class Datafile_Grandin_Fetus(Datafile_Grandin):
    """
    General structure of Grandin 2018 fetus datafiles
   
    """
    mapping = {
        'CEF_ngml': 'BPS',
        'CEFconj_ngml': 'BPSG',
        'CEF_d8_ngml': 'BPS-d8' , 
        'CEFconj_d8_ngml': 'BPSG-d8',
    }
    header = 0
    index_col = 0

    def get_title(self, parameter):
        mapping = {
            'CEF_ngml': 'fetus BPS',
            'CEF_conj_ngml': 'fetus BPSconj',
            'CEF_d8_ngml': 'fetus BPS-d8' , 
            'CEF_conj_d8_ngml': 'fetus BPAconj-d8',
        }
     
        return self.title % (self.experiment, mapping[parameter]) 
    
    
class Datafile_Grandin_Mother_Exp1(Datafile_Grandin_Mother):
    datafile = "../aggregation_BPS/experiment1_mother_aggregated.csv"
    experiment = 'Experiment #1'

    
class Datafile_Grandin_Mother_Exp2(Datafile_Grandin_Mother):
    datafile = "../aggregation_BPS/experiment2_mother_aggregated.csv"
    experiment = 'Experiment #2'
    
class Datafile_Grandin_Fetus_Exp1(Datafile_Grandin_Fetus):
    datafile = "../aggregation_BPS/experiment1_fetus_aggregated.csv"
    experiment = 'Experiment #1'
    
class Datafile_Grandin_Fetus_Exp2(Datafile_Grandin_Fetus):
    datafile = "../aggregation_BPS/experiment2_fetus_aggregated.csv"
    experiment = 'Experiment #2'
    
    
class Datafile_Grandin_Mother_Exp1_ngml(Datafile_Grandin_Mother):
    datafile = "../aggregation_BPS/experiment1_mother_aggregated_ngml.csv"
    experiment = 'Experiment #1'

class Datafile_Grandin_Mother_Exp2_ngml(Datafile_Grandin_Mother):
    datafile = "../aggregation_BPS/experiment2_mother_aggregated_ngml.csv"
    experiment = 'Experiment #2'
    
class Datafile_Grandin_Fetus_Exp1_ngml(Datafile_Grandin_Fetus):
    datafile = "../aggregation_BPS/experiment1_fetus_aggregated_ngml.csv"
    experiment = 'Experiment #1'
    
class Datafile_Grandin_Fetus_Exp2_ngml(Datafile_Grandin_Fetus):
    datafile = "../aggregation_BPS/experiment2_fetus_aggregated_ngml.csv"
    experiment = 'Experiment #2'
    
#class DatafileCorbel(Datafile):
#    """
#    General structure of Corbel 2013 datafiles
#    
#    """
#    mapping = {
#        'CA_nM': 'mBPA_C',
#        'CA_conj_nM': 'mBPAG_C',
#        'CA_fetus_nM': 'fBPA_C' , 
#        'CA_conj_fetus_nM': 'fBPAG_C',
#    }
#
#    def get_title(self, parameter):
#        mapping = {
#            'CA_nM': 'mother BPA',
#            'CA_conj_nM': 'mother BPAconj',
#            'CA_fetus_nM': 'fetus BPA' , 
#            'CA_conj_fetus_nM': 'fetus BPAconj',
#        }
#     
#        return self.title % mapping[parameter] 
#
#
#    
#class Datafile_Corbel_Mother_BPA(DatafileCorbel):
#    """
#    Corbel experiment #1
#    
#        IV administration of BPA to mother
#    """
#    datafile = '../corbel_mother_bpa.csv'
#    header = 0
#    title = 'Corbel: IV BPA to mother --> %s [nM]'
#
#
#
#class Datafile_Corbel_Mother_BPAG(DatafileCorbel):
#    """
#    Corbel experiment #2
#    
#        IV administration of BPAG to mother
#    """
#    datafile = '../corbel_mother_bpag.csv'
#    header = 0
#    title = 'Corbel: IV BPAconj to mother --> %s [nM]'
#
#   
#    
#class Datafile_Corbel_Fetus_BPA(DatafileCorbel):
#    """
#    Corbel experiment #3 - IV administration
#    
#        IV administration of BPA to fetus
#    """
#    datafile = '../corbel_fetus_bpa.csv'
#    header = 0
#    title = 'Corbel: IV BPA to fetus --> %s [nM]'
#
#
#    
#class Datafile_Corbel_Fetus_BPAG(DatafileCorbel):
#    """
#    Corbel experiment #4
#    
#        IV administration of BPAG to fetus
#    """
#    datafile = '../corbel_fetus_bpag.csv'
#    header = 0
#    title = 'Corbel: IV BPAconj to fetus --> %s [nM]'
#
#
