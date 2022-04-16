funcprot(0);

function [a0,A,B]=fourierplot(l,n,f)
clf();

a0 = 1/l*intg(-l,l,f,.000000001,0.00001);
for i=1:n
	function b=f1(x,f)
	b=f(x)*cos(i*%pi*x/l);
endfunction
function c=f2(x,f)
	c=f(x)*sin(i*%pi*x/l);
endfunction

A(i)=1/l*intg(-l,l,f1,.000000001,0.00001);
B(i)=1/l*intg(-l,l,f2,.000000001,0.00001);
end

function series=solution(x)
	series=a0/2;
	for i=1:n
		series=series+A(i)*cos(i*%pi*x/l)+B(i)*sin(i*%pi*x/l);
	end
endfunction

x=-5*l:0.1:5*l;
plot(x,solution(x));
endfunction

deff('a=f(x)','a=x');
[A0,A,B]=fourierplot(2,100,f)
