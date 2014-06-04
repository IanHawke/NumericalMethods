%
% function phi = Worksheet6_MyShootingPhi(dvdx, z)
%
% Utility function for the shooting method
%
function phi = Worksheet6_MyShootingPhi(dvdx, z)

% Check the input is reasonable
if (not(isa(dvdx, 'function_handle')))
    error('First argument must be a function handle!')
end

[t, y] = ode45(dvdx, [0 1], [0;z]);
phi = y(end,1) - 1;

end