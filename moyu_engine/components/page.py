
class Page():
    def __init__(self,config={
                                    'page':'page_data',
                                }):
        self.config = config

    def set(self,page):
        return self.config.get(page,'/=/ Page Erro /=/ Out Of Range')

if __name__=="__main__":
    page = Page()
    page.config['page_add'] = 'page_add'
    print(page.set('page_add'))