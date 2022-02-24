import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    inp = ""
    msgs = [["Nice to meet you!", "User"],["Hello!","Bot"],["Who are you?", "User"],["I am an advising chatbot.","Bot"]]
    postId = ""
    constructor(private http: HttpClient){}

    ngOnInit(): void {
    }
    
    onGoToSubmit() {

      this.msgs.push([this.inp, "User"])
      this.http.post("http://localhost:8000",this.inp,{responseType: 'text'}).subscribe(data => {
        console.log(data)
        this.msgs.push([data, 'Bot'])
      })
      this.inp = ""
      
    }


}
