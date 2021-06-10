{$MODE DELPHI}
program parser;
{
    CS 3304 Project 1
    Abu Jalloh
}


uses SysUtils, StrUtils;

var
    input : String; {input string}
    idx : Integer; {current index for tokenized input array}
    arrL : Integer; {length of string array}
    nt: String; {next token}
    output : String; {final output string}
    stringArray: TStringArray; {array of input string using space delimiter}
    invalidT : boolean; {flag for bad token}
  
    
procedure nounPhrase; FORWARD;

function notValid(): boolean;
begin
    if (((nt <> 'lifted') and (nt <> 'saw' ) and (nt <> 'found' )) and
        ((nt <> 'quickly') and (nt <> 'carefully' ) and (nt <> 'brilliantly' )) and
            ((nt <> 'cow') and (nt <> 'alice' ) and (nt <> 'book' )) and
                ((nt <> 'mean') and (nt <> 'lean' ) and (nt <> 'green' )) and
                    ((nt <> 'of') and (nt <> 'at' ) and (nt <> 'with' ))) then
                        notValid := true
    else
        notValid := false;
end;
    
procedure lexical; {advances to the next token}
begin
    idx := idx + 1;
    
    if idx < arrL then
        nt := stringArray[idx];

     if (notValid) then
        invalidT := true;

    
end;

procedure verbPhrase; {parses verb phrase}
begin
    
    output := output + '(';
    if ((nt = 'lifted') or (nt = 'saw' ) or (nt = 'found' )) then
        begin
            output := output + '"' + nt + '"';
            lexical;
        end;
    
    if ((nt = 'quickly') or (nt = 'carefully' ) or (nt = 'brilliantly' )) then
        begin
            output := output + '"' + nt + '"';
            lexical;
        end;
    output := output + ')';
    
end;

procedure parse; {adds token to output and advances to next token}
begin
    output := output + '"' + nt + '"';
    lexical;

end;

procedure adjPhrase; {parses adj phrase}
begin
    if ((nt = 'green') or (nt = 'lean' ) or (nt = 'mean' )) then
        begin
            output := output + '(';
            parse;
            adjPhrase;
            output := output + ')';
        end
    else
        
end;


procedure prepPhrase; {parses prep phrase}
begin
    if ((nt = 'of') or (nt = 'at' ) or (nt = 'with' )) then
        begin
            output := output + '(';
            parse;
            nounPhrase;
            output := output + ')';
        end;

end;

procedure nounPhrase; {parses noun phrase}
begin
    output := output + '(';
    if ((nt = 'green') or (nt = 'lean' ) or (nt = 'mean' )) then
        adjPhrase;
    if ((nt = 'alice') or (nt = 'cow' ) or (nt = 'book' )) then
        parse;
    if ((nt = 'of') or (nt = 'at' ) or (nt = 'with' )) then
        prepPhrase;
    output := output +  ')';

end;

procedure parseSentence; {parses full sentence}
begin
    
    output := output + '((';
    nounPhrase;
    output := output + ') ';
    
    verbPhrase;
    
    output := output + ' (';
    nounPhrase;
    output := output + '))';
    

end;

begin
    readln(input);
    invalidT := false;
    
    stringArray := input.Split(' ');
   { stringArray := TStringArray.Create('Billy', 'found', 'green','book');}
    arrL := Length(stringArray);
    
    idx := 0;
    nt := stringArray[0];
    
    if (notValid) then
        invalidT := true;
                    
    output := '';
    
    parseSentence;
    
    if(invalidT) then
        writeln('Input has invalid tokens.')
    else
        writeln(output);
    

end.