from bs4 import BeautifulSoup, Tag 
from urllib.request import Request, urlopen

# my libraries
import containers



class Extractor(object):
    '''
    This class can extract information from the website
    and store them into a data structure (dict)
    '''
    def __init__(self, url):
        # open the url and parse with bs4
        req = Request(
            url=url, 
            headers={'User-Agent': 'Mozilla/5.0'}
            )
        page = urlopen(req)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        self.p_content = soup.find("div", {"id":"page4"})
        self.content = soup.find("div", {"id":"page8"})
        # initialize opening status of each level
        self.principle_open = False
        self.guideline_open = False 
        self.criteria_open = False
        # 4 principles
        self.principles = ['perceivable', 'operable', 'understandable', 'robust']
        self.p_messages = []
        for p in p_content.find_all("h4"):
            p = str(p.string) # convert to unicode
            self.p_messages.append(p[8:])
        self.g_amount = [4, 5, 3, 1] # guideline amount for each principle
        # data structure for storing information
        self.DATA = {}
        
    def extract():
        def process_ins(href):
            """
            submethod to process the inspection pages
            Input:
                href: string, the link to inspection page
            Output:
                InspectionCode: container.InspectionCode object
            """
        def process_eval(href):
            """
            submethod to process the evaluation pages
            Input:
                href: string, the link to evaluation page
            Output:
                EvaluationCode: container.EvaluationCode object
            """
        # initialization
        p_index = 0
        guidelines = {}
        g_index = 0
        g_count = 0
        # fixed amount of guideline for each principle
        for g_header in self.content.find_all('h4'):
            # put guidelines in principle when amount is fulfilled 
            if (g_count == self.g_amount[g_index]):  
                p = self.principles[p_index]
                message = self.p_messages[p_index]
                self.DATA[p] = containers.principle(p, message, guidelines)
                guidelines = {}
                g_count = 0
                g_index += 1
            # otherwise keep creating guideline object
            g_id = g_header['id']
            g_message = g_header.find_next_sibling('p')
            next_tag = guideline.find_next_sibling(['h4', 'h5'])
            criterias = {}
            # take in all the criterias until next guideline header
            while (next_tag.tag != 'h4'):
                c_header = next_tag
                c_id = c_header['id']
                c_message = c_header.find_next_sibling('p')
                inspections = {}
                evaluations = {}
                # Inspection codes
                ins_code = None
                ins_header = c_header.find_next_sibling(is_ins)
                if (has_children_codes(ins_header)):
                    for li in ins_header.find_next_sibling('ul').children:
                        if type(li) != Tag:
                            continue
                        if li.find('a'):
                            ins_code = process_ins(li.find('a')['href'])
                            inspections[ins_code.id] = ins_code
                # Evaluation codes
                eval_code = None`
                eval_header = c_header.find_next_sibling(is_eval)
                if (has_children_codes(eval_header)):
                    for li in eval_header.find_next_sibling('ul').children:
                        if type(li) != Tag:
                            continue
                        if li.find('a'):
                            eval_code = process_eval(li.find('a')['href'])
                            evaluations[eval_code.id] = eval_code
                criterias[c_id] = container.Criteria(c_id, c_message, inspections, evaluations)

            guidelines[g_id] = containers.guideline(g_id, g_message, criterias)
                
    def check_open(level):
        """
        Input
            level: string, which level to check the status
        Ouput
            True or False
        """
        if level == "principle":
            return self.principle_open
        elif level == "guideline":
            return self.guideline_open
        elif level == "criteria":
            return self.criteria_open
        else:
            print("wrong usage of 'check' method")
            return -1 


