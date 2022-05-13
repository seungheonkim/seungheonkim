from 게시판.member.service import MemberService

#menu
class Mem_Menu:
    def __init__(self):
        self.service = MemberService()

    def run(self):
        while True:
            m = input('1.회원가입 2.로그인 3.내정보확인 4.수정 5.로그아웃 6.탈퇴 7.종료')
            if m == '1':
                self.service.addMember()
            elif m == '2':
                self.service.login()
            elif m == '3':
                self.service.printMyInfo()
            elif m == '4':
                self.service.editMem()
            elif m == '5':
                self.service.logout()
            elif m == '6':
                self.service.delMem()
            elif m == '7':
                break