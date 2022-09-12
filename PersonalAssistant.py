class PersonalAssistant:
  
  def __init__(self, todos, birthdays, contacts):
    
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
      return f'{todo_item} was removed'
    else: 
      print("To-do is not on list!")
    

  def get_todos(self):
        return self.todos

  def get_birthdays(self):
        return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return f"Sorry can't find a birthday for this person."
    

  def add_birthday(self, name, date):
    if name in self.birthdays: 
        return f"You already have a birthday for {name}"
    else: 
        self.birthdays[name] = date
        return f"{name}'s birthday has been addded"

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed."
    else:
      return f"Sorry there is no recorded birthday for that person."

  
  def get_contact(self, name):
    if name in self.contacts: 
        return f"{name} is a {self.contacts[name]}"
    else:
        return "There is no contact with that name"

 
  def add_contact(self, name, job_position):
    if name in self.contacts: 
        return f"You already have information for {name}"
    else: 
        self.contacts[name] = job_position
        return f"{name}'s information has been addded"

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s information has been removed."
    else:
      return f"Sorry there is no recorded information for that person."

  def get_contacts(self):
    return self.contacts

      
    
    
      
    
      
      
