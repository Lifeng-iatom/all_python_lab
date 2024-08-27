class Employee:
      def __init__(self,name,email_address,title,phone_number=None):
            self.name = name
            self.email_address =email_address
            self.title = title
            self.phone_number = phone_number

      def email_signature(self,include_phone=True):
            if self.phone_number and include_phone:
                  return f"{self.name} - {self.title}\n{self.email_address} ({self.phone_number})"
            else:
                  return f"{self.name} - {self.title}\n{self.email_address}"
