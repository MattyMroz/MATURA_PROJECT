/*
Napisz program zamieniający wyrazenie algebraiczne zapisane w notacji tradycyjnej
na wyrazenie zapisane w odwrotnej notacji polskiej. Wyrazenie moze sie skladac
z argumentow jednoznakowych (liter i liczb jednocyfrowych), nawiasow okraglych
oraz dwuargumentowych dzialan arytmetycznych: dodawania (+), odejmowania (−),
mnozenia (*), wyznaczania czesci calkowitej z dzielenia (/) oraz potegowania (^).
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

string ONP(string w)
{
    stack<char> stos;
    stos.push('#');
    string onp = "";

    for(int i = 0; i < w.size(); i++)
    {
        switch(w[i])
        {
        case '(':
            stos.push('(');
            break;
        case ')':
            while(stos.top() != '(')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.pop();
            break;
        case '+':
            while(stos.top() != '#' && stos.top() != '(')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.push('+');
            break;
        case '-':
            while(stos.top() != '#' && stos.top() != '(')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.push('-');
            break;
        case '*':
            while(stos.top() == '*' || stos.top() == '/' || stos.top() == '^')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.push('*');
            break;
        case '/':
            while(stos.top() == '*' || stos.top() == '/' || stos.top() == '^')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.push('/');
            break;
        case '^':
            if(stos.top() == '^')
            {
                onp = onp + stos.top();
                stos.pop();
            }
            stos.push('^');
            break;
        default:
            onp = onp + w[i];
        }
    }

    while(stos.top() != '#')
    {
        onp = onp + stos.top();
        stos.pop();
    }
    stos.pop();

    return onp;
}

int main()
{
    string w;
    cout << "Podaj wyrazenie algebraiczne w notacji tradycyjnej: ";
    cin >> w;
    cout << "Wyrazenie w ONP: " << ONP(w) << endl;
    return 0;
}
