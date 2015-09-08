class FASTAReader(object):
    def __init__(self,file):
        self.file=file #store file
        self.last_ident = None #store previously encountered header
        
    def next(self): #return ID and sequence.
        if self.last_ident is None:
            line=self.file.readline() 
            assert line.startswith(">"), "Not valid fasta"
            ident = line[1:].rstrip("\r\n")
        else:
            ident=self.last_ident

        sequences=[]
        while True: #loops forever as long as the expression is true
            line=self.file.readline()
            if not line: #if line = "', encountered a last line
                break
            if line.startswith(">"): #will break if line starts with the header character 
                self.last_ident = line[1:].rstrip("\r\n") 
                break
            else:
                sequences.append(line.strip()) #remove all the white space from the beginning and end. just sequen
        if len(sequences) == 0:
            raise StopIteration 
        
        sequence="".join( sequences )
        return ident, sequence

    def __iter__(self):
        return self