''' Tässä voidaan lisätä koulutusohjelmaan kursseja ja niiden välisiä esitietovaatimuksia sekä löytää jokin tapa
käydä kurssit läpi niin, että aina kun otetaan käsittelyyn uusi kurssi, on sen esitiedot käyty. Koska ongelma 
palautuu suunattuun syklittömään graafiin (tai sykli tarkoittaa, että ongelma ei ratkea), voidaan käyttää 
syvyyshakua, jota toistetaan aina, kun löydetään kurssi, jonka tila ei ole 2, joka tarkoittaa ratkennutta. Tilaa 1 käytetään
kun solmu on otettu käsittelyyn mutta sen kaikkia naapureita ei ole vielä käyty läpi. Ykköseen törmääminen uudelleen
karakterisoi kehäriippuvuuden. '''

class CoursePlan:
    def __init__(self):
        
        self.neighbors = dict()
        self.course_list = []

    def add_course(self,course):
        
        self.neighbors[course] = []

    def add_requisite(self,course1,course2):
    
        self.neighbors[course1].append(course2)

    def find(self):
        
        visited = {course: 0 for course in self.neighbors}
        self.course_list = []

        def traverse(course):

            if visited[course] == 2:
                return
            elif visited[course] == 1:
                return True
            else:
                visited[course] = 1
                for neighbor in self.neighbors[course]:
                    if traverse(neighbor):
                        return True
                visited[course] = 2
                self.course_list.append(course)

        for course in self.neighbors:

            if visited[course] == 2:
                continue
            else:
                if traverse(course) == True:
                    return None
                
        if len(self.course_list) == len(self.neighbors):

            return self.course_list[::-1]
        
        else:

            return None

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course('course1')
    c.add_course('course2')
    c.add_requisite('course1','course2')
    c.add_course('course3')
    c.add_requisite('course1','course3')
    print(c.find())
    print(c.find())
    c.add_course('course4')
    c.add_course('course5')
    c.add_requisite('course4','course5')