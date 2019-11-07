/*
Copyright (C) 2019  Antonio José Grandson Busson (Telemidia/PUC-Rio)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


var colors = [ 
    [255, 0, 0],
    [0, 0, 255],
    [0, 255, 0],
    [255, 255, 0],
    [255, 0, 255],
    [0, 255, 255],
    [255, 255, 255]
];

function getColorByInt(index){
    return colors[index]; 
}