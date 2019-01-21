class Protozoan:
    NUMBER_OF_GENES = 10
    GENE_MIN_VALUE = 0
    GENE_MAX_VALUE = 5
    def __init__(self, given_name, genelist):
        self.__name = given_name
        self.__genes= []
        
        if (len(genelist) > Protozoan.NUMBER_OF_GENES ):

            for i in range(Protozoan.NUMBER_OF_GENES):
                self.__genes.append(Protozoan.GENE_MIN_VALUE)
            return 
        else:
            genelist_sorted = sorted(genelist)
            
            if(genelist_sorted[-1]>Protozoan.GENE_MAX_VALUE):
                for i in range(Protozoan.NUMBER_OF_GENES):
                    self.__genes.append(Protozoan.GENE_MIN_VALUE) 
                return
            else:
                self.__genes = genelist.copy() 
                                
        
    def get_name(self):
        return self.__name
    def get_genes(self):

        return self.__genes
    def mutation(self, gene_no, new_gene):
        #Changes the protozoan's gene indicated by the index given 
        # as parameter gene_no to a new value indicated by 
        # the parameter new_gene. The mutation succeeds only if 
        # the number of the gene is in the range 0-9 and if the
        # new value for the gene is in the range 0-5. If the mutation succeeds,
        # the method returns True. Otherwise the method doesn't do anything and returns False.
        if gene_no in range(0,9):
            if(new_gene in range(0,6)):
                self.__genes[gene_no]=new_gene
                return True
            else:
                return False
    def clone(self, clone_name):
        #Creates and returns a new Protozoan-object which has an exact copy 
        # of the current protozoan's genes (remember how list references work).
        #  The name of the new protozoan is given as parameter.
        new_genes = self.__genes.copy()
        return Protozoan(clone_name,new_genes)

    def mate(self, another_protozoan, descendant_name):
        #Creates a new Protozoan-object, which gets the genes 0, 2, 4, 6 and 8 from 
        #the current protozoan and the rest of the genes from the protozoan given
        #as parameter (the numbers indicate indices in the gene list).
        #The name of the new protozoan is given as the last parameter.
        #The method returns the new Protozoan-object (technically a reference to it).
        new_protozoa= another_protozoan.get_genes()[:]
        for i in (0,2,4,6,8):
            new_protozoa[i] = self.__genes[i]             
        
        return Protozoan(descendant_name,new_protozoa)
    def __str__(self):
        str1 = "Name: "+self.__name + ", genes: " + str(self.__genes)
        return str1
