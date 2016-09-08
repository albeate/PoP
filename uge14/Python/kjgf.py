
plt.ion()
plt.figure()
plt.xlabel('Beholder radius: 10')
#plt.ylabel('Y - akse tekst')
plt.title('Uge 14 Aflevering ',fontsize=20)
count = 0
while count <150:
    plt.clf()    
    beholder=plt.Circle((0,0),10,color='black',fill=False)
    fig = plt.gcf()
    fig.gca().add_artist(beholder)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    #print 'count:',count
    liste_old = liste_new
    liste_new =[]
    count += 1
    nummer = 0
    #Opgave c:

    #Opgave d
    liste_mod_vec = ny_vektor_hastighed(liste_old,m,T) #opgave d beregning -
                                                            #hvor vektor lÊngde skal Êndres
    for element in liste_mod_vec:
        nummer = nummer+1
        p_old=element[0]
        v_old=element[1]
        if nummer == 1:
            plt.plot(p_old[0], p_old[1], '+',color='r') # Tegn et punkt
            plt.draw() # Bed pyplot om at tegne figuren
        if nummer == 2:
            plt.plot(p_old[0], p_old[1], '*',color='blue') # Tegn et punkt
            plt.draw() # Bed pyplot om at tegne figuren
        if nummer == 3:
            plt.plot(p_old[0], p_old[1], '+',color='blue') # Tegn et punkt
            plt.draw() # Bed pyplot om at tegne figuren
        if nummer == 4:
            plt.plot(p_old[0], p_old[1], '.',color='black') # Tegn et punkt
            plt.draw() # Bed pyplot om at tegne figuren
        if nummer == 5:
            plt.plot(p_old[0], p_old[1], '+',color='green') # Tegn et punkt
            plt.draw() # Bed pyplot om at tegne figuren
        p_new,v_new = next_position(p_old,v_old,c,radius,t_delta)
        partikel_new=[p_new,v_new]
        liste_new.append(partikel_new)

plt.ioff()

