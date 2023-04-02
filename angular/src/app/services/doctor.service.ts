import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Doctor } from '../models/doctor.model';

const baseUrl = 'http://localhost:8000/api/Doctors';
const summaryUrl = 'http://localhost:8000/api/Doctors_Summary'
const all_summary_Url='http://localhost:8000/api/All_Doctors_Summary'

@Injectable({
  providedIn: 'root'
})

export class DoctorService {
  constructor(private http: HttpClient) { }


  getAll(): Observable<any> {
    return this.http.get(baseUrl);
  }

  // getAll(): Observable<any> {
  //   return this.http.get<Client[]>(baseUrl);
  // }

  get(id: any): Observable<Doctor> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByDoctorName(doctor_name: any): Observable<Doctor[]> {
    return this.http.get<Doctor[]>(`${baseUrl}?doctor_name_keyword=${doctor_name}`);
  }

  get_Doctor_Summary(id: any): Observable<Doctor> {
    return this.http.get(`${summaryUrl}/${id}`);
  }

  get_all_doctor_summaries(): Observable<any> {
    return this.http.get(all_summary_Url);
  }

}

