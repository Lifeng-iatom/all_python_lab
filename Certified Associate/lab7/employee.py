class Employee:
      default_db_file ="employee_file.txt"
      def __init__(self, name, email_address, title, phone_number=None,identifier=None):
            self.name = name
            self.email_address = email_address
            self.title = title
            self.phone_number = phone_number
            self.identifier = identifier

      def email_signature(self, include_phone=False):
            signature = f"{self.name} - {self.title}\n{self.email_address}"
            if include_phone and self.phone_number:
                  signature += f" ({self.phone_number})"
            return signature

      @classmethod
      def get_all(cls,file_name=None):
            result = []
            if not file_name:
                  file_name = cls.default_db_file
            with open(file_name,'r') as f:
                  lines = [
                        line.strip("\n").split(",") + [index + 1]
                        for index, line in enumerate(f.readlines())
                  ]
            for line in lines:
                  result.append(cls(*line))
            return result
      
      @classmethod
      def get_at_line(cls,line_number,file_name=None):
            
            if not file_name:
                  file_name = cls.default_db_file

            with open(file_name,'r') as f:
                  line = f.readlines()[line_number-1]
                  one_line = line.strip("\n").split(',') + [line_number]
                  return (cls(*one_line))
      
      def save(self,file_name = None):
            if not file_name:
                  file_name = self.default_db_file
            with open(file_name,'r+') as f:
                  lines = f.readlines()
                  if self.identifier:
                        #update a line
                        lines[self.identifier - 1] =  self._database_lines()
                  else:
                        #add a new line
                        lines.append(self._database_lines())
                  f.seek(0)
                  f.writelines(lines)
      def _database_lines(self):
            return(
                  ",".join(
                        [self.name,self.email_address,self.title,self.phone_number or ""]
                  ) + "\n"
            )
                  
           
            