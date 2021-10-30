P = int(input('Enter Prime Number P: '))
G = int(input('Enter Prime Number G: '))


a = int(input('Enter Private KeyA for Alice: '))
x = int(pow(G,a,P))

b = int(input('Enter Private KeyB for Bob: '))
y = int(pow(G,b,P))

ka = int(pow(y,a,P))

kb = int(pow(x,b,P))

print('The public key for Alice is: ',x)
print('The public key for Bob is: ',y)

print('Secret key for Alice is : %d'%(ka))
print('Secret Key for Bob is : %d'%(kb))
