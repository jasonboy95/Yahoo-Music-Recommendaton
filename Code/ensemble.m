function [ Y ] = ensemble(S,Acc )
temp=inv(S'*S);
B=120000*(2*Acc-1);
A=temp*B;
Y=S*A;

end

