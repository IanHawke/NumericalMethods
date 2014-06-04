%
% Suggested model answers to worksheet 5
%
% Ian Hawke, 15/4/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; AB2

disp('Question 1')

f = @(x,y)(2 - exp(-4.*x)-2*y);
y0 = 1;
Nconvergence = 10;
y = zeros(Nconvergence, 1);
errs = zeros(size(y));
Npoints = zeros(size(y));
options.startup = 'Euler';
for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet5_MyAB2(f, y0, [0 1], Nsteps, options);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.1./Npoints.^2,'b-')
legend('AB2', '\propto h^2','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for AB2, Euler start up')

y = zeros(Nconvergence, 1);
errs = zeros(size(y));
Npoints = zeros(size(y));
options.startup = 'Euler PC';
for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet5_MyAB2(f, y0, [0 1], Nsteps, options);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
figure
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.1./Npoints.^2,'b-')
legend('AB2', '\propto h^2','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for AB2, Euler PC start up')


% Coding question 2; AM2

disp('Question 2')

y = zeros(Nconvergence, 1);
errs = zeros(size(y));
Npoints = zeros(size(y));
options.startup = 'Euler';
for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet5_MyAM2(f, y0, [0 1], Nsteps, options);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
figure
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.1./Npoints.^2,'b-')
legend('AM2', '\propto h^2','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for AM2, Euler start up')

y = zeros(Nconvergence, 1);
errs = zeros(size(y));
Npoints = zeros(size(y));
options.startup = 'Euler PC';
for i=1:Nconvergence
    Nsteps = 10*2^(i-1);
    Npoints(i) = Nsteps;
    y(i) = Worksheet5_MyAM2(f, y0, [0 1], Nsteps, options);
    errs(i) = abs(y(i) - 1 + (exp(-2) - exp(-4))/2);
end
figure
loglog(1./Npoints, errs, 'kx', 1./Npoints, 0.1./Npoints.^2,'b-')
legend('AM2', '\propto h^2','Location','SouthEast')
xlabel('h');ylabel('|Error|')
title('Convergence for AM2, Euler PC start up')


