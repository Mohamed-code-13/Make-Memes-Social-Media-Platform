document.querySelector('.b').disabled = true;
document.querySelector('.i').onkeyup = function()
{
    if (document.querySelector('.i').value === '')
    {
        document.querySelector('.b').disabled = true;
    } else {
        document.querySelector('.b').disabled = false;
    }
}