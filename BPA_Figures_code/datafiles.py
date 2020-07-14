import pandas as pd


class Datafile(object):
    datafile = None
    title = None
    delimiter = ','
    header = None
    columns = None
    
    mapping = {}
    
    def __init__(self, drop=None):
        self.df = pd.read_csv(
            self.datafile,
            delimiter=self.delimiter,
            header=self.header,
            names=self.columns,
        )
        
        if drop is not None:
            drop = drop + ['%s_Sd' % x for x in drop]
            self.df = self.df.drop(columns=drop)
        
        # all the variables within the datafile
        #      excluding time and all the standard deviations
        self.set_variables()
        
    def set_variables(self):
        self.inv_mapping = {v: k for k, v in self.mapping.items()}
        self.variables = self.df.columns.copy()
        self.variables = self.variables[self.variables != 'time']
        self.variables = self.variables[~self.variables.str.endswith('_Sd')]

    def get_title(self, parameter):
        return self.title
    
    
class DatafileScaler(Datafile):
    def __init__(self, datafile, scale):
        self.df = datafile.df.copy()
        self.mapping = datafile.mapping
        self.title = datafile.title
        
        # all columns but time need to be scaled
        columns = list(self.df.columns.values)
        index = columns.index('time')
        columns = columns[0:index] + columns[index+1:]
        
        # scale each column
        for column in columns:
            self.df[column] = scale*datafile.df[column]
            
        self.set_variables()


class Datafile_VeigaLopez_Mother(Datafile):
    datafile = "../experimental_data/A006_BPA_Maternal.txt"
    delimiter = '\t'
    columns = ['time', 'C', 'C_Sd']
    title = 'Veiga-Lopez: Total BPA + BPAconj in mother [ng/ml]'
    
    mapping = {
        'CA_plasma_ngml_mBPAtotal': 'C',
    }
    
    
class Datafile_VeigaLopez_Fetus(Datafile):
    datafile = "../experimental_data/A006_BPA_Fetal.txt"
    delimiter = '\t'
    header = None
    columns = ['time', 'C', 'C_Sd']
    title = 'Veiga-Lopez: Total BPA + BPAconj in fetus [ng/ml]'
    
    mapping = {
        'CA_plasma_ngml_fBPAtotal': 'C', 
    }

    
class DatafileCorbel(Datafile):
    """
    General structure of Corbel 2013 datafiles
    
    """
    mapping = {
        'CA_plasma_ngml_mBPA': 'mBPA_C',
        'CA_plasma_ngml_mBPAconj': 'mBPAG_C',
        'CA_plasma_ngml_fBPA': 'fBPA_C' , 
        'CA_plasma_ngml_fBPAconj': 'fBPAG_C',
    }

    def get_title(self, parameter):
        mapping = {
            'CA_plasma_ngml_mBPA': 'mother BPA',
            'CA_plasma_ngml_mBPAconj': 'mother BPAconj',
            'CA_plasma_ngml_fBPA': 'fetus BPA' , 
            'CA_plasma_ngml_fBPAconj': 'fetus BPAconj',
        }
     
        return self.title % mapping[parameter] 


    
class Datafile_Corbel_Mother_BPA(DatafileCorbel):
    """
    Corbel experiment #1
    
        IV administration of BPA to mother
    """
    datafile = '../experimental_data/corbel_mother_bpa.csv'
    header = 0
    title = 'Corbel: IV BPA to mother --> %s [nM]'



class Datafile_Corbel_Mother_BPAG(DatafileCorbel):
    """
    Corbel experiment #2
    
        IV administration of BPAG to mother
    """
    datafile = '../experimental_data/corbel_mother_bpag.csv'
    header = 0
    title = 'Corbel: IV BPAconj to mother --> %s [nM]'

   
    
class Datafile_Corbel_Fetus_BPA(DatafileCorbel):
    """
    Corbel experiment #3 - IV administration
    
        IV administration of BPA to fetus
    """
    datafile = '../experimental_data/corbel_fetus_bpa.csv'
    header = 0
    title = 'Corbel: IV BPA to fetus --> %s [nM]'


    
class Datafile_Corbel_Fetus_BPAG(DatafileCorbel):
    """
    Corbel experiment #4
    
        IV administration of BPAG to fetus
    """
    datafile = '../experimental_data/corbel_fetus_bpag.csv'
    header = 0
    title = 'Corbel: IV BPAconj to fetus --> %s [nM]'








class Datafile_Corbel_Mother_BPA_ngml(DatafileCorbel):
    """
    Corbel experiment #1
    
        IV administration of BPA to mother
    """
    datafile = '../experimental_data/corbel_mother_bpa_ngml.csv'
    header = 0
    title = 'Corbel: IV BPA to mother --> %s [nM]'



class Datafile_Corbel_Mother_BPAG_ngml(DatafileCorbel):
    """
    Corbel experiment #2
    
        IV administration of BPAG to mother
    """
    datafile = '../experimental_data/corbel_mother_bpag_ngml.csv'
    header = 0
    title = 'Corbel: IV BPAconj to mother --> %s [nM]'

   
    
class Datafile_Corbel_Fetus_BPA_ngml(DatafileCorbel):
    """
    Corbel experiment #3 - IV administration
    
        IV administration of BPA to fetus
    """
    datafile = '../experimental_data/corbel_fetus_bpa_ngml.csv'
    header = 0
    title = 'Corbel: IV BPA to fetus --> %s [nM]'


    
class Datafile_Corbel_Fetus_BPAG_ngml(DatafileCorbel):
    """
    Corbel experiment #4
    
        IV administration of BPAG to fetus
    """
    datafile = '../experimental_data/corbel_fetus_bpag_ngml.csv'
    header = 0
    title = 'Corbel: IV BPAconj to fetus --> %s [nM]'


