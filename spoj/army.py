def battle(g, m, g_army, m_army):
    g_army.sort()
    m_army.sort()
    if g_army[0] == m_army[0]:
        del m_army[0]
        m -= 1
    elif g_army[0] < m_army[0]:
        del g_army[0]
        g -= 1
    else:  # if g_army[0] > m_army[0]:
        del m_army[0]
        m -= 1

    return g, m, g_army, m_army

        

def war(g, m, g_army, m_army):
    while(g > 0 and m > 0):
        g, m, g_army, m_army = battle(g, m, g_army, m_army)
    if g > 0:
        print "Godzilla"
    else:
        print "MechaGodzilla"


def process():
    t = int(raw_input())
    for _ in range(t):
        raw_input()  # blank line
        g, m = map(int, raw_input().split())
        g_army = map(int, raw_input().split())
        m_army = map(int, raw_input().split())
        war(g, m, g_army, m_army)

process()
