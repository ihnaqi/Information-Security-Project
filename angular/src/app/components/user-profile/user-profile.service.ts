import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { AuthService } from '../user-login/auth.service';

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {

  constructor(private http: HttpClient) { }

  getUserProfile(userId: string|null): Observable<any> {

    
    
    return this.http.get(`http://localhost:8000/api/patient/dashboard`);
  }
}