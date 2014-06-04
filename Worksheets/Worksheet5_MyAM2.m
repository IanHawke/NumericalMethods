%
% function t = Worksheet5_MyAM2(f, y0, interval, Nsteps, options)
%
% Solve the ODE y' = f(x, y) on the given interval taking Nsteps with
% initial data y0.
%
function yend = Worksheet5_MyAM2(f, y0, interval, Nsteps, options)

% Check the input is reasonable
if (not(isa(f, 'function_handle')))
    error('First argument must be a function handle!')
elseif ((not(isnumeric(interval)))&&(ndims(interval)~=1)&&(length(interval)~=2))
    error('Second argument must define the interval; a 1d length 2 numeric array!')
elseif (not(isstruct(options)))
    error('Final argument must be an options structure!')
elseif (not(isfield(options,'startup')))
    error('startup field must be set in the options!')
end

h = (interval(2) - interval(1)) / Nsteps;
x = linspace(interval(1), interval(2), Nsteps+1);
y = zeros(size(x));
y(1) = y0;

switch (options.startup)
   
    case 'Euler'
        % A single Euler step
        y(2) = y(1) + h * f(x(1), y(1));
    case 'Euler PC'
        % A single Euler predictor-corrector step
        yp   = y(1) + h * f(x(1), y(1));
        y(2) = y(1) + h/2 * (f(x(1), y(1)) + f(x(2), yp));
    otherwise
        error('Need to set options.startup to a recognized value!')
    
end

for i = 2:Nsteps
    % AB 2 to predict
    yp = y(i) + h * (3 * f(x(i), y(i)) - f(x(i-1), y(i-1))) / 2;
    % AM 2 to correct
    y(i+1) = y(i) + h * (f(x(i+1), yp) + f(x(i), y(i))) / 2;
end

yend = y(end);

end
