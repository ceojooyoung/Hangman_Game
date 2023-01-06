import pygame
import os
import random

# 게임 윈도우 크기
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20221557 박주영 HW2")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 효과음 로드
sound = pygame.mixer.Sound(os.path.join(assets_path, 'sound.wav'))
scream = pygame.mixer.Sound(os.path.join(assets_path, 'scream.mp3'))
clap = pygame.mixer.Sound(os.path.join(assets_path, 'clap.mp3'))
shortscream = pygame.mixer.Sound(os.path.join(assets_path, 'shortscream.mp3'))
            
# 게임 종료 전까지 반복
done = False

#정답 리스트 및 게임 로직 사전 세팅
Ans = ['', 'korea', 'japan', 'china', 'vietnam', 'thai', 'cambodia', 'mongolia', 'india', 'pakistan', 'iran', \
    'russia', 'france', 'germany', 'spain', 'italy', 'swiss', 'poland', 'israel', 'igypt', 'sudan', \
        'canada', 'mexico', 'brazil']

ipt = ' '
iptcnt=0
gameover = False
correct = False
Ans_num = 0    
Wrong_num = 0
Notin=[]
Answered=[]
screamplayed = False

# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and iptcnt==0:
            if event.key==pygame.K_a :ipt='a';iptcnt=1
            elif event.key==pygame.K_b:ipt='b';iptcnt=1
            elif event.key==pygame.K_c:ipt='c';iptcnt=1
            elif event.key==pygame.K_d:ipt='d';iptcnt=1
            elif event.key==pygame.K_e:ipt='e';iptcnt=1
            elif event.key==pygame.K_f:ipt='f';iptcnt=1
            elif event.key==pygame.K_g:ipt='g';iptcnt=1
            elif event.key==pygame.K_h:ipt='h';iptcnt=1
            elif event.key==pygame.K_i:ipt='i';iptcnt=1
            elif event.key==pygame.K_j:ipt='j';iptcnt=1
            elif event.key==pygame.K_k:ipt='k';iptcnt=1
            elif event.key==pygame.K_l:ipt='l';iptcnt=1
            elif event.key==pygame.K_m:ipt='m';iptcnt=1
            elif event.key==pygame.K_n:ipt='n';iptcnt=1
            elif event.key==pygame.K_o:ipt='o';iptcnt=1
            elif event.key==pygame.K_p:ipt='p';iptcnt=1
            elif event.key==pygame.K_q:ipt='q';iptcnt=1
            elif event.key==pygame.K_r:ipt='r';iptcnt=1
            elif event.key==pygame.K_s:ipt='s';iptcnt=1
            elif event.key==pygame.K_t:ipt='t';iptcnt=1
            elif event.key==pygame.K_u:ipt='u';iptcnt=1
            elif event.key==pygame.K_v:ipt='v';iptcnt=1
            elif event.key==pygame.K_w:ipt='w';iptcnt=1
            elif event.key==pygame.K_x:ipt='x';iptcnt=1
            elif event.key==pygame.K_y:ipt='y';iptcnt=1
            elif event.key==pygame.K_z:ipt='z';iptcnt=1
            elif event.key == pygame.K_SPACE : 
                #정답 리스트를 모두 소모하면 승리 
                if len(Ans) == 0 :
                    clap.play(-1)
                    done=True
                #정답을 맞췄을 경우 다음 스테이지로 초기화
                elif correct == True :
                    gameover = False
                    correct = False
                    del Ans[Ans_num]
                    Ans_num = 0    
                    Wrong_num = 0
                    Notin=[]
                #게임 종료 시 창 닫기
                elif gameover == True : done = True
        elif event.type == pygame.KEYUP : 
            ipt=' '
            iptcnt=0

    # 게임 로직 구간
    # 게임 진행 중
    if gameover == False:
        if Ans_num!=0 and Ans[0] == Ans[Ans_num] : 
            if correct == False : 
                Answered.append(Ans[Ans_num])
                clap.play()
            correct = True
        #한 판 시작 전 초기화
        elif Ans_num==0 :
            if Ans!=[] : 
                Ans_num = random.randint(1,len(Ans)-1)
                Ans[0] = ' '*len(Ans[Ans_num])
            Wrong_num = 0
            Notin=[]
        #한 판 플레이
        elif Wrong_num < 7 :
            if ipt in Notin or ipt in Ans[0] : continue 
            elif ipt in Ans[Ans_num] :
                sound.play()
                for i in range(len(Ans[Ans_num])) :
                    if Ans[Ans_num][i] == ipt :
                        if i==0 : Ans[0] = ''.join(list(ipt)+list(Ans[0][1:]))
                        elif i==len(Ans[Ans_num])-1 : Ans[0] = ''.join(list(Ans[0][:i])+list(ipt))
                        else: Ans[0] = ''.join(list(Ans[0][:i])+list(ipt)+list(Ans[0][i+1:]))
            elif ipt not in Ans[Ans_num]:
                Notin+=ipt
                Notin+=' '                        
                Wrong_num+=1
                if Wrong_num < 7 and correct == False : shortscream.play()
        #한 판 종료
        elif Wrong_num >= 7 : 
            gameover = True
    else : 
        if screamplayed == False and correct == False :
            scream.play()
            screamplayed = True

    # 윈도우 화면 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간
    # 교수대 그리기
    pygame.draw.line(screen, (0,0,0), [90, 660], [330, 660], 20)
    pygame.draw.line(screen, (0,0,0), [210, 660], [210, 240], 20)
    pygame.draw.line(screen, (0,0,0), [200, 240], [430, 240], 20)
    pygame.draw.line(screen, (0,0,0), [420, 240], [420, 330], 20)

    #행맨 그리기
    if Wrong_num>=1 or gameover == True: pygame.draw.circle(screen, BLACK, [420, 330], 30, 0)
    if Wrong_num>=2 or gameover == True: pygame.draw.line(screen, BLACK, [420,350], [420, 390], 10)
    if Wrong_num>=3 or gameover == True: pygame.draw.line(screen, BLACK, [420,390], [360,450], 15)
    if Wrong_num>=4 or gameover == True: pygame.draw.line(screen, BLACK, [420,390], [480,450], 15)
    if Wrong_num>=5 or gameover == True: pygame.draw.line(screen, BLACK, [420, 390], [420, 480], 20)
    if Wrong_num>=6 or gameover == True: pygame.draw.line(screen, BLACK, [420,480], [360, 570], 20)
    if gameover == True : pygame.draw.line(screen, BLACK, [420,480], [480, 570], 10)

    #UI
    for i in range(len(Ans[Ans_num])) : pygame.draw.line(screen, BLACK, [180+60*i,180], [210+60*i, 180], 10)
    #폰트 설정
    font = pygame.font.SysFont("arial", 20, True, False)
    Message = pygame.font.SysFont("arial", 50, True, False)

    #Basic UI Text
    screen.blit(Message.render("HANGMAN GAME", True, BLACK, WHITE), (180, 30))
    screen.blit(font.render("Answer(country) : ", True, BLACK, WHITE), [40, 140])
    screen.blit(font.render("Not In : ", True, BLACK, WHITE), [40, 100])
    screen.blit(font.render("Left : "+str(len(Ans)-1), True, BLACK, WHITE), [600, 210])
    screen.blit(font.render("Answered", True, BLACK, WHITE), [600, 240])
    for i in range(len(Answered)) :
        screen.blit(font.render(Answered[i], True, BLACK, WHITE), [600, 260+20*i])
    
    #Game Message Text
    if correct == True :
        screen.blit(Message.render("Congratuation!", True, (0,0,255), WHITE), [200, WINDOW_HEIGHT//2])
        screen.blit(Message.render("Press Space Key to Next step", True, (0,0,255), WHITE), [80, WINDOW_HEIGHT//2+60])
    elif gameover == True : 
        screen.blit(Message.render("Game Over!", True, (255,0,0), WHITE), [240, WINDOW_HEIGHT//2])
        screen.blit(Message.render("Press Space Key to Close Window", True, (255,0,0), WHITE), [30, WINDOW_HEIGHT//2+60])
    else:
        for i in range(len(Ans[Ans_num])) :
            screen.blit(font.render(Ans[0][i], True, BLACK, WHITE), [195+60*i, 150])
        for i in range(len(Notin)) :
            screen.blit(font.render(Notin[i], True, (0,0,0), (255,255,255)), [110+15*i, 100])

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 수만큼 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()