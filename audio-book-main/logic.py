import re

class Document:
    def __init__(self, title, author, content_text):
        self.title = title
        self.author = author
        self.content_text = content_text
    
    def process_content(self):
        '''აბსტრაქტული მეთოდი, რომელსაც მიიღებს ყველა შვილი კლასი და თავისებურად დაამუშავებს ტექსტს.
        თუ რომელიმე შვილ კლასს დაავიწყდება ამ მეთოდის გადაწერა, პროგრამა მუშაობისას ამ ერორს ისვრის:'''
        raise NotImplementedError("The child class is missing the process content!.")
    
class Ebook(Document):
    def __init__(self, title, author, content_text, genre):
        super().__init__(title, author, content_text)
        self.genre = genre

    def process_content(self):
        """regex პოულობს თავებს შემდეგი ფორმატით: Chapter 1, Chapter I, chapter I, თავი 1, თავი I..."""

        chapter_pattern = r'(?i)\b(?:chapter|თავი)\s*(?:\d+|[IVXLCDM]+)\b'
        
        #finditerით ვპოულობთ ყველა თავს
        markers = list(re.finditer(chapter_pattern, self.content_text))  #marker ცვლადში ინახება ყველა თავის მარკერი, რომლებზეც იტერაციას მოვახდენთ
        
        #თუ მოხდა გაუთვალისწინებელი შემთხვევა და თავები ვერ იპოვა, მთლიან ტექსტს ვაბრუნებთ ერთ ნაწილად
        if not markers:
            return [{"title": "Main Content", "text": self.content_text.strip()}]
            
        chapters = [] #ამ ცვლადში შეინახება თავები და ტექსტები შემდეგნაირად:  ["title: Chapter I, text: "თავის სრული ტექსტი..."]
        
        #თუ პირველ თავამდე არის რაიმე შესავალი ტექსტი
        if markers[0].start() > 0:  #თუ თავის აღმნიშვნელი სიტყვის პირველი ასო 0 ინდექსზე არ გვხვდება:
            intro_text = self.content_text[:markers[0].start()].strip()  #ნულოვანი ინდექიდან პირველი თავის წინა ასომდე ყველაფერს იყებს და სტრიპით აშორებს ზედმეტებს
            if intro_text:
                chapters.append({"title": "Introduction", "text": intro_text})
        
        #სათითაოდ ვჭრით ტექსტს თავებს შორის
        for i in range(len(markers)):
            start_pos = markers[i].start()   #რომელ ინდექსზე იწყება კონკრეტული თავი

            #თუ ეს არ არის ბოლო თავი
            if i + 1 < len(markers):
                end_pos = markers[i+1].start()  #დასასრული არის შემდეგი თავის დასაწყისი
            else:
                #თუ ბოლო თავია
                end_pos = len(self.content_text) #დასასრული არის მთლიანი წიგნის ბოლო ასო
            
            chapter_title = markers[i].group().strip()   #ყოველ იტერაციაზე ვიგებთ მიმდინარე თავის ნუმერაციას
            
            #თავის სათაურს ვაცლით ტექსტის ნაწილს და ვიტოვებთ მხოლოდ მის შიგთავსს
            chapter_text = self.content_text[markers[i].end():end_pos].strip()
            
            chapters.append({
                "title": chapter_title,
                "text": chapter_text
            })
            
        return chapters
    

class Essay(Document):
    def __init__(self, title, author, content_text):
        super().__init__(title, author, content_text)
        

    def process_content(self):
        pattern = r'\n+'
        markers = list(re.finditer(pattern, self.content_text))

        if not markers:
            return [{"title": self.title, "text": self.content_text.strip()}]

        chapters = []

        chapters.append({
            "title": "Paragraph 1",
            "text": self.content_text[:markers[0].start()].strip()
        })

        for i in range(len(markers)):
            start_pos = markers[i].end()
            end_pos = markers[i + 1].start() if i + 1 < len(markers) else len(self.content_text)

            chapters.append({
                "title": f"Paragraph {i + 2}",
                "text": self.content_text[start_pos:end_pos].strip()
            })

        return chapters