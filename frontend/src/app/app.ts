// src/app/app.ts
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  filename = '';
  sessionId = '';
  question = '';
  answer = '';
  loading = false;
  fileSummary = '';
  selectedFile!: File;
  uploading=false;

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadFile() {
    if (!this.selectedFile) return;

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.uploading = true;

    this.http.post<any>('http://localhost:8000/api/upload/', formData).subscribe({
      next: (res) => {
        console.log(res)
        this.filename = this.selectedFile.name;
        this.sessionId = res.session_id;
        this.fileSummary = res.summary;
        this.uploading = false;
      },
      error: () => {
        this.fileSummary = 'Upload failed.';
        this.loading = false;
      },
    });
  }

  ask() {
    if (!this.question.trim() || !this.sessionId) return;

    this.loading = true;
    this.answer = '';

    this.http
      .get<any>(`http://localhost:8000/api/ask/`, {
        params: { q: this.question, session_id: this.sessionId },
      })
      .subscribe({
        next: (res) => {
          this.answer = res.answer;
          console.log(res)
          this.loading = false;
        },
        error: () => {
          this.answer = 'Error occurred';
          this.loading = false;
        },
      });
  }

  reset() {
    this.filename = '';
    this.sessionId = '';
    this.question = '';
    this.answer = '';
    this.fileSummary = '';
    this.selectedFile = undefined!;
  }
}
