class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password


    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f'User Name: {self.name}\n User Job: {self.current_job_title}')


user_one = User('valami@sdfsdf.com', 'nana Jos', 'pde123', 'DevOps')
user_two = User('dzson@pop.com', 'Josh', 'pde123', 'IT Manager')

user_one.get_user_info()




